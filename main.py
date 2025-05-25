import os
import asyncio
import logging
from fastapi import FastAPI

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

app = FastAPI()


@app.get("/")
async def healthcheck():
    return {"status": "ok"}


@app.on_event("startup")
async def on_startup():
    logging.basicConfig(level=logging.INFO)
    await db.init_db_pool()
    await db.create_tables()

    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        logging.error("TELEGRAM_BOT_TOKEN is not set!")
        return

    bot = Bot(token=token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    # Регистрируем роутеры
    dp.include_router(start_router)
    dp.include_router(instruction_router)
    dp.include_router(price_router)
    dp.include_router(cosmetics_router)
    dp.include_router(booking_router)
    dp.include_router(text_router)
    dp.include_router(voice_router)

    # Регистрируем slash-команды для меню слева
    await bot.set_my_commands([
        BotCommand(command="book", description="Онлайн-бронювання"),
        BotCommand(command="price", description="Прайс-лист"),
        BotCommand(command="cosmetics", description="Меню косметики"),
        BotCommand(command="instruction", description="Інструкція використання бота"),
    ])

    # Запускаем polling
    asyncio.create_task(dp.start_polling(bot))


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
