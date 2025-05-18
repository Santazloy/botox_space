# handlers/text.py

from aiogram import Router, types, F
from aiogram.enums import ChatAction
import html
import re
import db

from config import PRICE_KEYWORDS, BOOKING_KEYWORDS_UA
from utils.gpt import generate_gpt_reply_ua
from utils.contact import send_contact_info_message
from handlers.price import show_price_groups
from handlers.booking import cmd_book
from handlers.cosmetics import entry_to_cosmetics, cosmetics_faq, BRAND_KEYWORDS, SUBGROUP_KEYWORDS

router = Router()

# паттерн для вопросов по брендам/категориям косметики
COSMETICS_TRIGGER = [
    "косметика", "крем", "мазі", "препарати", "засіб", "сировотка", "бренди"
]
COSMETICS_PATTERN = re.compile(r"(?i)(" +
                               "|".join(BRAND_KEYWORDS + SUBGROUP_KEYWORDS) +
                               r")")


@router.message(F.text)
async def handle_text(message: types.Message):
    user_id = message.from_user.id
    text = message.text
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

    if reply.strip().startswith("<pre>") and reply.strip().endswith("</pre>"):
        await message.answer(reply, parse_mode="HTML")
    else:
        escaped = html.escape(reply)
        await message.answer(f"<pre>{escaped}</pre>", parse_mode="HTML")

    await send_contact_info_message(message)

    # 5) Триггер бронирования
    if any(k in txt_lower for k in BOOKING_KEYWORDS_UA):
        await message.answer("<pre>Зараз допоможу з бронюванням!</pre>",
                             parse_mode="HTML")
        await cmd_book(message)
