# handlers/voice.py

import os
import re
from aiogram import Router, types, F
from aiogram.enums import ChatAction
import db

from config import PRICE_KEYWORDS, BOOKING_KEYWORDS_UA
from utils.whisper import transcribe_with_gpt4o
from utils.gpt import generate_gpt_reply_ua
from utils.tts import send_voice_reply_ua
from utils.contact import send_contact_info_message
from handlers.price import show_price_groups
from handlers.booking import cmd_book
from handlers.cosmetics import entry_to_cosmetics, cosmetics_faq, BRAND_KEYWORDS, SUBGROUP_KEYWORDS

router = Router()

# составляем паттерн для косметических запросов
COSMETICS_TRIGGER = [
    "косметика", "крем", "мазі", "препарати", "засіб", "сировотка", "бренди"
]
COSMETICS_PATTERN = re.compile(r"(?i)(" +
                               "|".join(BRAND_KEYWORDS + SUBGROUP_KEYWORDS) +
                               r")")


@router.message(F.voice)
async def handle_voice(message: types.Message):
    user_id = message.from_user.id
    filename = f"voice_{message.message_id}.ogg"

    # загрузка и транскрипция
    await message.bot.download(file=message.voice.file_id,
                               destination=filename)
    text = await transcribe_with_gpt4o(filename)
    os.remove(filename)

    if not text:
        await message.answer("<pre>Не вдалося розпізнати голос.</pre>",
                             parse_mode="HTML")
        return

    lower = text.lower()
    await db.add_message_to_history(user_id, "user", text)

    # 1) Триггер прайсу
    if any(k in lower for k in PRICE_KEYWORDS):
        await show_price_groups(message)
        return

    # 2) Триггер меню косметики
    if any(k in lower for k in COSMETICS_TRIGGER):
        await entry_to_cosmetics(message)
        return

    # 3) Триггер вопросов по бренду/категории косметики
    if COSMETICS_PATTERN.search(text):
        await cosmetics_faq(message)
        return

    # 4) Общий GPT-ответ
    await message.bot.send_chat_action(message.chat.id,
                                       ChatAction.RECORD_VOICE)
    reply = await generate_gpt_reply_ua(user_id, text)
    await db.add_message_to_history(user_id, "assistant", reply)

    await send_voice_reply_ua(message, reply)
    await send_contact_info_message(message)

    # 5) Триггер бронирования
    if any(k in lower for k in BOOKING_KEYWORDS_UA):
        await cmd_book(message)
