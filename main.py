import os
import logging
import asyncio
from aiohttp import web
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand, Update

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

WEBHOOK_PATH = "/webhook"
BASE_WEBHOOK_URL = os.getenv("WEBHOOK_URL")
WEBHOOK_SECRET_TOKEN = os.getenv("WEBHOOK_SECRET", "supersecret")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = Bot(token=TELEGRAM_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

dp["bot"] = bot
dp["secret_token"] = WEBHOOK_SECRET_TOKEN

dp.include_router(start_router)
dp.include_router(instruction_router)
dp.include_router(price_router)
dp.include_router(cosmetics_router)
dp.include_router(booking_router)
dp.include_router(text_router)
dp.include_router(voice_router)

async def on_startup():
    await db.init_db_pool()
    await db.create_tables()
    webhook_url = f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}"
    try:
        await bot.set_webhook(
            url=webhook_url,
            secret_token=WEBHOOK_SECRET_TOKEN,
            drop_pending_updates=True
        )
        logging.info(f"Webhook установлен: {webhook_url}")
    except Exception as e:
        logging.error(f"Ошибка при установке webhook: {e}")

    # 📌 Регистрируем команды Telegram
    await bot.set_my_commands([
        BotCommand(command="start", description="Запуск бота"),
        BotCommand(command="price", description="Прайс-лист"),
        BotCommand(command="instruction", description="Как пользоваться"),
        BotCommand(command="cosmetics", description="Каталог косметики"),
        BotCommand(command="book", description="Онлайн-запись"),
    ])
    logging.info("Команды Telegram зарегистрированы.")


async def handle_webhook(request):
    try:
        if request.headers.get("X-Telegram-Bot-Api-Secret-Token") != WEBHOOK_SECRET_TOKEN:
            logging.warning("Неверный webhook секрет.")
            return web.Response(status=403)

        data = await request.json()
        update = Update.model_validate(data)
        await dp.feed_update(bot, update)
    except Exception as e:
        logging.exception("Ошибка обработки webhook")
        return web.Response(status=500)

    return web.Response(text="ok")

async def main():
    await on_startup()
    logging.info("Бот в режиме Webhook + Background Worker")

    app = web.Application()
    app.router.add_post(WEBHOOK_PATH, handle_webhook)

    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

    logging.info(f"Сервер запущен на http://localhost:{port}{WEBHOOK_PATH}")
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
