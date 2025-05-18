# video.py

import logging
from aiogram import Router, types
from aiogram.filters import Command
from aiogram import F

logger = logging.getLogger(__name__)

video_router = Router()


@video_router.message(Command("vid"), F.video)
async def handle_vid_command(message: types.Message):
    """
    Обробник для команди /vid.
    Якщо до повідомлення прикріплене відео,
    бот повертає file_id цього відео.
    """
    # Беремо file_id із об'єкта video
    video_file_id = message.video.file_id
    logger.info(f"Video file_id: {video_file_id}")

    # Відповідаємо користувачу
    await message.answer(f"Video file_id: <pre>{video_file_id}</pre>",
                         parse_mode="HTML")
