# handlers/price.py
from aiogram import Router, F, types
from aiogram.enums import ChatAction, ParseMode
from aiogram.types import InputMediaVideo
from aiogram.utils.keyboard import InlineKeyboardBuilder
import db

from config import VIDEO_FILE_ID, SECTION_SEPARATOR
from data.price_sections import GROUPS, SECTION_DEFINITIONS
from utils.price import parse_service_line, format_price_item
from utils.gpt import generate_gpt_reply_ua
from utils.message_manager import dynamic_send
from aiogram.filters import Command

router = Router()


@router.message(Command("price"))  # ← slash-команда
async def cmd_price(message: types.Message):
    """
    Обработчик команды /price
    """
    await show_price_groups(message)


@router.message(F.text.regexp(r"(?i)прайс|ціна|вартість|вартіс"))
async def show_price_groups(message: types.Message):
    """
    Шаг 1: отправляем новое видео с кнопками основных групп прайса.
    """
    builder = InlineKeyboardBuilder()
    for grp in GROUPS:
        builder.button(text=f"{grp['emoji']} {grp['title']}",
                       callback_data=f"price_group:{grp['id']}")
    builder.adjust(2)

    await dynamic_send(bot=message.bot,
                       chat_id=message.chat.id,
                       user_id=message.from_user.id,
                       send_func=message.answer_video,
                       video=VIDEO_FILE_ID,
                       caption="🌟 <b>Оберіть категорію прайсу</b> 🌟",
                       parse_mode=ParseMode.HTML,
                       reply_markup=builder.as_markup())


@router.callback_query(F.data == "price_back")
async def on_back(callback: types.CallbackQuery):
    """
    Кнопка «Назад» к списку групп — редактируем то же видео-сообщение.
    """
    builder = InlineKeyboardBuilder()
    for grp in GROUPS:
        builder.button(text=f"{grp['emoji']} {grp['title']}",
                       callback_data=f"price_group:{grp['id']}")
    builder.adjust(2)

    await callback.message.edit_caption(
        caption="🌟 <b>Оберіть категорію прайсу</b> 🌟",
        parse_mode=ParseMode.HTML,
        reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data.startswith("price_group:"))
async def on_group(callback: types.CallbackQuery):
    """
    Шаг 2: показываем подразделы выбранной группы + «Назад».
    """
    group_id = callback.data.split("price_group:", 1)[1]
    subs = [s for s in SECTION_DEFINITIONS if s["group"] == group_id]

    builder = InlineKeyboardBuilder()
    for sec in subs:
        builder.button(text=f"{sec['emoji']} {sec['title']}",
                       callback_data=f"price_section:{sec['id']}")
    builder.button(text="🔙 Назад", callback_data="price_back")
    builder.adjust(1)

    await callback.message.edit_caption(caption="📂 <b>Оберіть підрозділ</b>",
                                        parse_mode=ParseMode.HTML,
                                        reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data.startswith("price_section:"))
async def on_section(callback: types.CallbackQuery):
    """
    Шаг 3: показываем услуги раздела в виде кнопок + «Назад».
    """
    section_id = callback.data.split("price_section:", 1)[1]
    sec = next((s for s in SECTION_DEFINITIONS if s["id"] == section_id), None)
    if not sec:
        await callback.answer("Розділ не знайдено.", show_alert=True)
        return

    items = [l.strip() for l in sec["raw_text"].splitlines() if l.strip()]
    builder = InlineKeyboardBuilder()
    for idx, line in enumerate(items):
        parsed = parse_service_line(line)
        if parsed and not parsed["is_note"]:
            btn = format_price_item(parsed["name"], parsed["price"],
                                    parsed["currency"])
        else:
            btn = parsed["name"] if parsed else line
        builder.button(text=btn,
                       callback_data=f"price_item:{section_id}:{idx}")
    builder.button(text="🔙 Назад", callback_data=f"price_group:{sec['group']}")
    builder.adjust(1)

    await callback.message.edit_caption(
        caption=f"<b>{sec['emoji']} {sec['title']}</b>\n{SECTION_SEPARATOR}",
        parse_mode=ParseMode.HTML,
        reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data.startswith("price_item:"))
async def on_item(callback: types.CallbackQuery):
    """
    Шаг 4: пользователь выбрал услугу — удаляем прошлое сообщение и
    публикуем новое с описанием и кнопкой «Назад».
    """
    _, section_id, idx_str = callback.data.split(":", 2)
    idx = int(idx_str)

    sec = next(s for s in SECTION_DEFINITIONS if s["id"] == section_id)
    items = [l.strip() for l in sec["raw_text"].splitlines() if l.strip()]
    line = items[idx]

    user_id = callback.from_user.id
    await db.add_message_to_history(user_id, "user", f"Опис процедури: {line}")
    await callback.bot.send_chat_action(callback.message.chat.id,
                                        ChatAction.TYPING)
    reply = await generate_gpt_reply_ua(user_id, f"Опис процедури: {line}")
    await db.add_message_to_history(user_id, "assistant", reply)

    # Отправляем новое сообщение вместо старого
    text = f"**_{line}_**\n\n{reply}"
    builder = InlineKeyboardBuilder()
    builder.button(text="🔙 Назад",
                   callback_data=f"price_back_section:{section_id}")
    builder.adjust(1)

    await dynamic_send(bot=callback.bot,
                       chat_id=callback.message.chat.id,
                       user_id=user_id,
                       send_func=callback.message.answer,
                       text=text,
                       parse_mode=ParseMode.MARKDOWN,
                       reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data.startswith("price_back_section:"))
async def on_back_section(callback: types.CallbackQuery):
    """
    Кнопка «Назад» в описании услуги:
    удаляем описание и вновь показываем видео+кнопки услуг раздела.
    """
    section_id = callback.data.split("price_back_section:", 1)[1]
    sec = next(s for s in SECTION_DEFINITIONS if s["id"] == section_id)
    items = [l.strip() for l in sec["raw_text"].splitlines() if l.strip()]

    user_id = callback.from_user.id
    # Отправляем видео-меню раздела как новое сообщение
    builder = InlineKeyboardBuilder()
    for idx, line in enumerate(items):
        parsed = parse_service_line(line)
        if parsed and not parsed["is_note"]:
            btn = format_price_item(parsed["name"], parsed["price"],
                                    parsed["currency"])
        else:
            btn = parsed["name"] if parsed else line
        builder.button(text=btn,
                       callback_data=f"price_item:{section_id}:{idx}")
    builder.button(text="🔙 Назад", callback_data=f"price_group:{sec['group']}")
    builder.adjust(1)

    await dynamic_send(
        bot=callback.bot,
        chat_id=callback.message.chat.id,
        user_id=user_id,
        send_func=callback.message.answer_video,
        video=VIDEO_FILE_ID,
        caption=f"<b>{sec['emoji']} {sec['title']}</b>\n{SECTION_SEPARATOR}",
        parse_mode=ParseMode.HTML,
        reply_markup=builder.as_markup())
    await callback.answer()
