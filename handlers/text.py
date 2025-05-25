# handlers/text.py
from aiogram import Router, types, F
from aiogram.enums import ChatAction
import re
import db

from config import PRICE_KEYWORDS, BOOKING_KEYWORDS_UA
from utils.gpt import generate_gpt_reply_ua
from utils.contact import send_contact_info_message
from handlers.price import show_price_groups
from handlers.booking import cmd_book
from handlers.cosmetics import entry_to_cosmetics, cosmetics_faq, BRAND_KEYWORDS, SUBGROUP_KEYWORDS
from utils.message_manager import dynamic_send

router = Router()

# паттерн для вопросов по брендам/категориям косметики
COSMETICS_TRIGGER = [
    "косметика", "крем", "мазі", "препарати", "засіб", "сировотка", "бренди"
]
COSMETICS_PATTERN = re.compile(
    r"(?i)(" + "|".join(BRAND_KEYWORDS + SUBGROUP_KEYWORDS) + r")"
)


@router.message(F.text)
async def handle_text(message: types.Message):
    user_id = message.from_user.id
    text = message.text.strip()
    txt_lower = text.lower()

    await db.add_message_to_history(user_id, "user", text)

    # 1) Триггер прайсу
    if any(k in txt_lower for k in PRICE_KEYWORDS):
        await show_price_groups(message)
        return

    # 2) Триггер меню косметики
    if any(k in txt_lower for k in COSMETICS_TRIGGER):
        await entry_to_cosmetics(message)
        return

    # 3) Триггер вопросов по бренду/категории косметики
    if COSMETICS_PATTERN.search(text):
        await cosmetics_faq(message)
        return

    # 4) Общий GPT-ответ
    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    reply = await generate_gpt_reply_ua(user_id, text)
    await db.add_message_to_history(user_id, "assistant", reply)

    # Отправляем ответ GPT: HTML с жирными заголовками и курсивом под ними
    await dynamic_send(
        bot=message.bot,
        chat_id=message.chat.id,
        user_id=user_id,
        send_func=message.answer,
        text=reply,
        parse_mode="HTML"
    )

    # Контактная информация
    await send_contact_info_message(message)

    # 5) Триггер бронирования
    if any(k in txt_lower for k in BOOKING_KEYWORDS_UA):
        await dynamic_send(
            bot=message.bot,
            chat_id=message.chat.id,
            user_id=user_id,
            send_func=message.answer,
            text="<b>Зараз допоможу з бронюванням!</b>",
            parse_mode="HTML"
        )
        await cmd_book(message)
