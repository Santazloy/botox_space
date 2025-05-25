# handlers/booking.py
from aiogram import Router, types
from aiogram.enums import ChatAction
from aiogram.filters import Command  # или CommandStart
from aiogram.fsm.context import FSMContext

from utils.message_manager import dynamic_send

router = Router()


@router.message(Command("book"))  # или CommandStart()
async def cmd_book(message: types.Message, state: FSMContext):
    # обязательно тело функции
    await dynamic_send(bot=message.bot,
                       chat_id=message.chat.id,
                       user_id=message.from_user.id,
                       send_func=message.answer,
                       text="Добре, розпочнемо бронювання…")
