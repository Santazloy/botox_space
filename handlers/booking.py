from aiogram import Router, types
from aiogram.enums import ChatAction
from aiogram.filters import Command  # или CommandStart
from aiogram.fsm.context import FSMContext

router = Router()


@router.message(Command("book"))  # или CommandStart()
async def cmd_book(message: types.Message, state: FSMContext):
    # обязательно тело функции
    await message.answer("Добре, розпочнемо бронювання…")
