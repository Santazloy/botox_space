# handlers/start.py
from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
from config import VIDEO_FILE_ID  # Імпорт вашого відео
from utils.message_manager import dynamic_send

router = Router()


@router.message(CommandStart())
@router.message(Command(commands=["menu"]))
async def cmd_start(message: types.Message):
    caption = (
        "<b>👋 Вітаємо в «Botox Space»!</b>\n\n"
        "🤖 <b>Бот відповідає текстом на текстові повідомленя і голосом на голосові</b>, завжди готовий проконсультувати з будь-якого питання з косметології.\n\n"
        "🔹 <b>Напишіть або відправте голосове повідомлення “прайс” / “ціна”</b> — перегляд вартості процедур.\n"
        "🔹 <b>Напишіть або відправте голосове повідомлення зі словами “косметика” / “бренд”</b> — меню косметичних засобів.\n\n"
        "🗓️ <b>Онлайн-бронювання:</b>\n"
        "   • Запис онлайн: <a href=\"http://n220793.alteg.io/company\">n220793.alteg.io/company</a>\n"
        "   • Телефон для запису: 0687075187\n\n"
        "⬇️⬇️⬇️ Або натисніть кнопку нижче ")
    await dynamic_send(bot=message.bot,
                       chat_id=message.chat.id,
                       user_id=message.from_user.id,
                       send_func=message.answer_video,
                       video=VIDEO_FILE_ID,
                       caption=caption,
                       parse_mode=ParseMode.HTML,
                       disable_web_page_preview=True)
