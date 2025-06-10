from dotenv import load_dotenv
import os
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)

# Telegram
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
if not TELEGRAM_BOT_TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN is not set in environment variables")

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is not set in environment variables")

# FFmpeg
FFMPEG_CMD = os.getenv("FFMPEG_PATH", "ffmpeg")
if not os.path.isfile(FFMPEG_CMD) and FFMPEG_CMD == "ffmpeg":
    logging.warning(f"FFmpeg binary '{FFMPEG_CMD}' not found in PATH; audio conversion may fail")

# TTS
TTS_API_ENDPOINT = os.getenv("TTS_API_ENDPOINT")
TTS_API_KEY = os.getenv("TTS_API_KEY")
if not TTS_API_ENDPOINT or not TTS_API_KEY:
    logging.warning("TTS API credentials (TTS_API_ENDPOINT or TTS_API_KEY) are missing")

# Video file default ID
VIDEO_FILE_ID = os.getenv(
    "VIDEO_FILE_ID",
    "BAACAgIAAxkBAAIBP2gnFMWOhb7-RhWVEyc8n0h1oasMAALJbAACxy85SUmQFGcM0dDyNgQ"
)

# Database
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL is not set in environment variables")

# Price utility keywords
NEW_PRICE_LINE_TOTAL_WIDTH = 48
MAX_SERVICE_NAME_LEN = 30
PRICE_KEYWORDS = [
    "прайс", "вартість", "вартіст", "вартіс", "варті", "прай",
    "ціна", "цін", "процедури", "послуги", "коштуе", "коштує", "коштуют"
]

# Booking utility keywords
BOOKING_KEYWORDS_UA = ["забронювати", "записатися", "бронювання", "запис"]

# System prompt for GPT utilities
SYSTEM_PROMPT_UA = (
    "Ти — Оксана, адміністратор косметологічного центру «Botox Space» у Львові. "
    "Ти чудово знаєш все про косметологію, ін'єкції, догляд за шкірою, епіляцію, масаж тощо. "
    "У твоєму центрі є розширений прайс із багатьох процедур. "
    "Відповідай виключно українською мовою, в дружньому та професійному тоні, "
    "надавай поради клієнтам, розповідай про різницю між процедурами і підкреслюй їхні переваги. "
    "Якщо запитують про ціни – запропонуй обрати розділ прайсу кнопками. "
    "Якщо хтось питає про власника чи відкриття центру – кажи, що директорка Тетяна дуже талановита людина, сама створила цей бізнес у Львові. "
    "Якщо хтось попросить розповісти про Тетяну – розкажи дивовижну історію з пригодами. "
    "Додавай трохи медичної термінології у відповіді про косметологію. "
    "Обов’язково вставляй у свій текст релевантні емодзі (🌸, 💆, 💧, ✨ тощо), "
    "щоб зробити відповідь живішою та приємнішою. "
    "Використовуй **жирний текст** для заголовків і *курсив* для підзаголовків."
)

SECTION_SEPARATOR = "───────────────"
