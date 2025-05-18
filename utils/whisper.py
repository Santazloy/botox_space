# utils/whisper.py

import openai
import asyncio
from config import OPENAI_API_KEY

async def transcribe_with_gpt4o(filename: str) -> str:
    """
    Транскрибирует аудио, используя GPT-4o Transcribe с жёсткой установкой украинского языка.
    Подсказка (prompt) bias-ит модель на ключевые слова прайса и бронювання.
    """
    openai.api_key = OPENAI_API_KEY
    try:
        with open(filename, "rb") as f:
            resp = await openai.Audio.atranscribe(
                model="gpt-4o-transcribe",  # переключаемся на GPT-4o Transcribe
                file=f,
                language="uk",              # явно указываем украинский
                prompt=(
                    "прайс, вартість, вартіст, вартіс, варті, прай, ціна, цін, "
                    "коштуе, коштує, коштуют, запис, бронювання"
                )
            )
        return resp["text"].strip()
    except Exception as e:
        # здесь можно логировать e, если нужно
        return ""