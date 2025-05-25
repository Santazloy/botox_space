# utils/message_manager.py

from aiogram import Bot
from aiogram.types import Message

# Для каждого пользователя храним ID последнего отправленного ботом сообщения
_last_message_ids: dict[int, int] = {}


async def dynamic_send(
    bot: Bot,
    chat_id: int,
    user_id: int,
    send_func: callable,
    *args,
    skip_delete_if_voice: bool = False,
    **kwargs,
) -> Message | None:
    """
    Отправляет новое сообщение, удаляя предыдущее для данного пользователя
    (если skip_delete_if_voice=False). Поддерживает методы Bot.send_* и Message.answer.
    Возвращает объект Message или None, если send_func не возвращает сообщение.
    """
    # Попытка удалить предыдущее сообщение
    prev_id = _last_message_ids.get(user_id)
    if prev_id and not skip_delete_if_voice:
        try:
            await bot.delete_message(chat_id, prev_id)
        except Exception:
            pass

    # Отправка нового сообщения
    if hasattr(send_func, "__self__") and isinstance(send_func.__self__, Bot):
        # Bot.send_* methods требуют chat_id первым аргументом
        msg = await send_func(chat_id, *args, **kwargs)
    else:
        msg = await send_func(*args, **kwargs)

    # Сохраняем ID, если объект Message
    if isinstance(msg, Message):
        _last_message_ids[user_id] = msg.message_id
    return msg
