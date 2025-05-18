# handlers/start.py

from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
from config import VIDEO_FILE_ID  # Імпорт вашого відео

router = Router()

@router.message(CommandStart())
@router.message(Command(commands=["menu"]))
async def cmd_start(message: types.Message):
    caption = (
        "<b>👋 Вітаємо в «Botox Space»!</b>\n\n"
        "🤖 <b>Бот відповідає текстом і голосом</b>, завжди готовий проконсультувати з будь-якого питання з косметології.\n\n"
        "🔹 <b>Напишіть “Price” / “ціна”</b> — перегляд вартості процедур.\n"
        "🔹 <b>Напишіть “косметика” / “бренд”</b> — меню косметичних засобів.\n\n"
        "🗓️ <b>Онлайн-бронювання:</b>\n"
        "   • Запис онлайн: <a href=\"http://n220793.alteg.io/company\">n220793.alteg.io/company</a>\n"
        "   • Телефон для запису: 0687075187\n\n"
    )
    await message.answer_video(
        video=VIDEO_FILE_ID,
        caption=caption,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )