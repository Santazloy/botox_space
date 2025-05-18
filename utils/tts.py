# utils/tts.py

import requests
import subprocess
import os
from aiogram.enums import ChatAction
from aiogram.types import FSInputFile
from config import TTS_API_KEY, TTS_API_ENDPOINT, FFMPEG_CMD


async def send_voice_reply_ua(message, text_for_voice: str):
    if not TTS_API_KEY or not TTS_API_ENDPOINT:
        return

    # Генерация opus-данных
    payload = {
        "input": text_for_voice,
        "voice": "sage",
        "response_format": "opus",
        "model": "tts-1-hd"
    }
    headers = {"Authorization": f"Bearer {TTS_API_KEY}"}
    resp = requests.post(TTS_API_ENDPOINT, json=payload, headers=headers)
    if resp.status_code != 200:
        return

    raw_opus = f"raw_{message.message_id}.opus"
    ogg_file = f"speech_{message.message_id}.ogg"

    # Сохраняем opus
    with open(raw_opus, "wb") as f:
        f.write(resp.content)

    # Конвертируем в OGG
    subprocess.run([
        FFMPEG_CMD, "-y", "-i", raw_opus, "-c:a", "libopus", "-ar", "48000",
        "-ac", "1", "-b:a", "64k", ogg_file
    ],
                   check=False)

    # Отправляем как файл
    await message.bot.send_chat_action(message.chat.id,
                                       ChatAction.UPLOAD_VOICE)
    await message.answer_voice(FSInputFile(ogg_file))

    # Удаляем временные файлы
    os.remove(raw_opus)
    os.remove(ogg_file)
