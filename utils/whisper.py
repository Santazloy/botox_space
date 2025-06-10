import openai
import subprocess
import os
import tempfile
import logging
import asyncio
from config import OPENAI_API_KEY, FFMPEG_CMD

logging.basicConfig(level=logging.INFO)

async def transcribe_with_gpt4o(filename: str) -> str:
    """
    Конвертирует OGG в WAV (16kHz, mono), затем транскрибирует с помощью whisper-1,
    выполняя до 5 попыток с экспоненциальным бэкоффом.
    """
    openai.api_key = OPENAI_API_KEY

    # Создание временного WAV-файла
    wav_temp = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
    wav_path = wav_temp.name
    wav_temp.close()

    # Конвертация OGG -> WAV
    try:
        subprocess.run([
            FFMPEG_CMD,
            '-y',
            '-i', filename,
            '-ar', '16000',
            '-ac', '1',
            wav_path
        ], check=True)
    except Exception as e:
        logging.exception(f"FFmpeg conversion failed: {e}")
        try:
            os.remove(wav_path)
        except OSError:
            pass
        return ""

    text = ""
    delay = 1
    # Попытки транскрипции
    for attempt in range(5):
        try:
            with open(wav_path, 'rb') as f:
                resp = await openai.Audio.atranscribe(
                    model="whisper-1",
                    file=f,
                    language="uk"
                )
            text = resp.get('text', '').strip()
            if text:
                break
        except Exception as e:
            logging.warning(f"Transcription attempt {attempt+1} failed: {e}")
            await asyncio.sleep(delay)
            delay *= 2

    if not text:
        logging.error("All transcription attempts failed.")

    # Удаляем временный WAV-файл
    try:
        os.remove(wav_path)
    except OSError:
        pass

    return text
