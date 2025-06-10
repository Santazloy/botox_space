import os
import logging
import asyncio
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand

import db
from handlers.start import router as start_router
from handlers.text import router as text_router
from handlers.voice import router as voice_router
from handlers.price import router as price_router
from handlers.booking import router as booking_router
from handlers.cosmetics import router as cosmetics_router
from handlers.instruction import router as instruction_router

load_dotenv()
logging.basicConfig(level=logging.INFO)

async def main():
    TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    bot = Bot(token=TELEGRAM_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp["bot"] = bot

    dp.include_router(start_router)
    dp.include_router(instruction_router)
    dp.include_router(price_router)
    dp.include_router(cosmetics_router)
    dp.include_router(booking_router)
    dp.include_router(text_router)
    dp.include_router(voice_router)

    await db.init_db_pool()
    await db.create_tables()

    await bot.set_my_commands([
        BotCommand(command="start", description="Запуск бота"),
        BotCommand(command="price", description="Прайс-лист"),
        BotCommand(command="instruction", description="Как пользоваться"),
        BotCommand(command="cosmetics", description="Каталог косметики"),
        BotCommand(command="book", description="Онлайн-запись"),
    ])
    logging.info("Команды Telegram зарегистрированы.")

    await dp.start_polling(bot, skip_updates=True)

if __name__ == "__main__":
    asyncio.run(main())
