# handlers/start.py
from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.enums import ParseMode
from config import VIDEO_FILE_ID  # Імпорт вашого відео
from utils.message_manager import dynamic_send
from handlers.instruction import INSTRUCTION_TEXT
from utils.tts import send_voice_reply_ua

router = Router()


@router.message(CommandStart())
@router.message(Command(commands=["menu"]))
async def cmd_start(message: types.Message):
    # Об'єднаний текст інструкції з контактами в одному підписі
    base_caption = (
        "<b>👋 Вітаю!</b>\n\n"
        "<b>Я — цифровий консультант косметологічного центру Botox Space.</b>\n"
        "Можу відповісти на будь-які ваші запитання про наш центр, процедури та їхню вартість,\n"
        "а також надати персоналізовану консультацію з урахуванням вашої проблеми і допомогти обрати оптимальне рішення.\n\n"
        "<b>💬 Як зі мною спілкуватися?</b>\n"
        "• Пишіть або надсилайте голосові повідомлення — я відповім у тому ж форматі.\n\n"
        "<b>💲 Щоб переглянути прайс:</b>\n"
        "Додайте до свого повідомлення ключове слово <b>«прайс»</b>, <b>«ціна»</b> або <b>«вартість»</b> —\n"
        "і ви отримаєте інтерактивне меню наших послуг.\n\n"
        "<b>🌸 Щоб ознайомитися з косметикою або продукцією:</b>\n"
        "Введіть <b>«бренд»</b>,  або <b>«продукція»</b> — і я покажу відповідні варіанти.\n\n"
        "<b>Дякую за увагу!</b>\n"
        "<b>Бажаю вам гарного дня від улюбленого Botox Space та вашої цифрової помічниці — Оксани.</b>\n"
        "<b>Все буде Україна! 🇺🇦</b>\n\n"
        "<b>──────────────</b>\n"
        "<b>🗓️ Онлайн-бронювання:</b>\n"
        "<b>   • Запис онлайн:</b> <a href=\"http://n220793.alteg.io/company\">n220793.alteg.io/company</a>\n"
        "<b>   • Телефон для запису:</b> 0687075187\n"
        "<b>──────────────</b>\n\n"
        "<b>📋 Якщо ви віддаєте перевагу класичному меню, натисніть кнопку «Меню»</b>\n"
        "⬇️⬇️⬇️ліворуч від поля введення тексту.\n\n"
    )

    # Надсилаємо відео з об'єднаним підписом
    await dynamic_send(
        bot=message.bot,
        chat_id=message.chat.id,
        user_id=message.from_user.id,
        send_func=message.answer_video,
        video=VIDEO_FILE_ID,
        caption=base_caption,
        parse_mode=ParseMode.HTML,
        disable_web_page_preview=True
    )

    # Озвучуємо ту саму інструкцію голосом
    await send_voice_reply_ua(message, INSTRUCTION_TEXT)
