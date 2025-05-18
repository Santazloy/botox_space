from aiogram import types
from aiogram.enums import ParseMode

async def send_contact_info_message(message: types.Message):
    text = (
        "✨ <b>Чекаємо на Вас!</b> ✨\n\n"
        "📞 <b>Для запису на процедури телефонуйте:</b>\n"
        "0687075187\n\n"
        "💻 <b>Або запишіться онлайн:</b>\n"
        "<a href=\"http://n220793.alteg.io/company\">Запис Онлайн</a>"
    )
    #await message.answer(text, parse_mode=ParseMode.HTML, disable_web_page_preview=True)