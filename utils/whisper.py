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

    # Конвертация OGG -> WAV
    wav_file = tempfile.NamedTemporaryFile(suffix='.wav', delete=False)
    wav_path = wav_file.name
    wav_file.close()
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
        return ""

    # Попытки транскрипции whisper-1 с экспоненциальным бэкоффом
    delay = 1
    for attempt in range(5):
        try:
            with open(wav_path, 'rb') as f:
                resp = await openai.Audio.atranscribe(
                    model="whisper-1",
                    file=f,
                    language="uk"
                )
            return resp.get('text', '').strip()
        except Exception as e:
            logging.warning(f"Transcription attempt {attempt+1} failed: {e}")
            await asyncio.sleep(delay)
            delay *= 2

    logging.error("All transcription attempts failed.")
    return ""

    finally:
        try:
            os.remove(wav_path)
        except OSError:
            pass
