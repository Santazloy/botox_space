# handlers/cosmetics.py
from aiogram import Router, F, types
from aiogram.filters.command import Command
from aiogram.enums import ChatAction
from aiogram.utils.keyboard import InlineKeyboardBuilder
import db

from config import VIDEO_FILE_ID
from data.cosmetics_sections import BRANDS, SUBGROUP_DEFINITIONS
from utils.gpt import generate_cosmetics_reply_ua
from utils.message_manager import dynamic_send

router = Router()


@router.message(Command("cosmetics"))
async def cmd_cosmetics(message: types.Message):
    """
    Обработчик команды /cosmetics — вызывает меню косметики.
    """
    await entry_to_cosmetics(message)


# ключевые слова для прямых запросов про бренд или подгруппу
BRAND_KEYWORDS = [
    "HydroPeptide", "Medik8", "Image", "Is Clinical", "Colorescience",
    "Revitalash", "Academie", "Histolab"
]
SUBGROUP_KEYWORDS = ["Сироватки", "Маски", "Крем", "SPF", "Очищення", "Eye"]
PATTERN = r"(?i)(" + "|".join(BRAND_KEYWORDS + SUBGROUP_KEYWORDS) + r")"


@router.message(
    F.text.regexp(r"(?i)косметика|бренд|засіб|сировотка|мазі|крем"))
async def entry_to_cosmetics(message: types.Message):
    """
    Триггер входа в меню косметики: отправляем новое сообщение
    с видео и кнопками всех брендов.
    """
    builder = InlineKeyboardBuilder()
    for b in BRANDS:
        builder.button(text=f"{b['emoji']} {b['title']}",
                       callback_data=f"cosm_brand:{b['id']}")
    builder.adjust(2)

    await dynamic_send(bot=message.bot,
                       chat_id=message.chat.id,
                       user_id=message.from_user.id,
                       send_func=message.answer_video,
                       video=VIDEO_FILE_ID,
                       caption="🌸 <b>Оберіть бренд косметики</b> 🌸",
                       parse_mode="HTML",
                       reply_markup=builder.as_markup())


@router.message(F.text.regexp(PATTERN))
async def cosmetics_faq(message: types.Message):
    """
    Если пользователь просто упомянул бренд или категорию —
    передаем его текст в GPT, отвечающего экспертом по этим брендам.
    """
    user_id = message.from_user.id
    text = message.text.strip()
    await db.add_message_to_history(user_id, "user", text)

    await message.bot.send_chat_action(message.chat.id, ChatAction.TYPING)
    reply = await generate_cosmetics_reply_ua(user_id, text)
    await db.add_message_to_history(user_id, "assistant", reply)

    await dynamic_send(bot=message.bot,
                       chat_id=message.chat.id,
                       user_id=user_id,
                       send_func=message.answer,
                       text=reply,
                       parse_mode="HTML")


@router.callback_query(F.data.startswith("cosm_brand:"))
async def on_brand(callback: types.CallbackQuery):
    """
    При выборе бренда: либо сразу список всех продуктов (если нет подгрупп),
    либо показываем кнопки подгрупп + «Назад».
    """
    brand_id = callback.data.split(":", 1)[1]
    subs = [s for s in SUBGROUP_DEFINITIONS if s["brand"] == brand_id]

    # нет подгрупп — сразу весь список
    if not subs:
        sec = next(s for s in SUBGROUP_DEFINITIONS
                   if s["brand"] == brand_id and s["id"].endswith("_all"))
        lines = [f"<b>{sec['emoji']} {sec['title']}</b>", ""
                 ] + sec["raw_text"].splitlines()
        await callback.message.edit_caption(caption="\n".join(lines),
                                            parse_mode="HTML",
                                            reply_markup=None)
        await callback.answer()
        return

    # есть подгруппы — строим кнопки
    builder = InlineKeyboardBuilder()
    for s in subs:
        builder.button(text=f"{s['emoji']} {s['title']}",
                       callback_data=f"cosm_sub:{s['id']}")
    builder.button(text="🔙 Назад", callback_data="cosm_back")
    builder.adjust(1)

    await callback.message.edit_caption(
        caption="📂 <b>Оберіть категорію продуктів:</b>",
        parse_mode="HTML",
        reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data == "cosm_back")
async def on_back(callback: types.CallbackQuery):
    """
    Кнопка «Назад» возвращает к списку брендов.
    """
    builder = InlineKeyboardBuilder()
    for b in BRANDS:
        builder.button(text=f"{b['emoji']} {b['title']}",
                       callback_data=f"cosm_brand:{b['id']}")
    builder.adjust(2)

    await callback.message.edit_caption(
        caption="🌸 <b>Оберіть бренд косметики</b> 🌸",
        parse_mode="HTML",
        reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data.startswith("cosm_sub:"))
async def on_sub(callback: types.CallbackQuery):
    """
    При выборе подгруппы показываем продукты как кнопки + «Назад».
    """
    sub_id = callback.data.split(":", 1)[1]
    sec = next(s for s in SUBGROUP_DEFINITIONS if s["id"] == sub_id)

    # строим кнопки продуктов
    items = [ln.strip() for ln in sec["raw_text"].splitlines() if ln.strip()]
    builder = InlineKeyboardBuilder()
    for idx, name in enumerate(items):
        builder.button(text=name, callback_data=f"cosm_prod:{sub_id}:{idx}")
    builder.button(text="🔙 Назад", callback_data=f"cosm_brand:{sec['brand']}")
    builder.adjust(1)

    await callback.message.edit_caption(
        caption=f"<b>{sec['emoji']} {sec['title']}</b>",
        parse_mode="HTML",
        reply_markup=builder.as_markup())
    await callback.answer()


@router.callback_query(F.data.startswith("cosm_prod:"))
async def on_product(callback: types.CallbackQuery):
    """
    При выборе продукта — запрашиваем описание в GPT и редактируем то же сообщение.
    """
    _, sub_id, idx = callback.data.split(":", 2)
    idx = int(idx)
    sec = next(s for s in SUBGROUP_DEFINITIONS if s["id"] == sub_id)
    products = [
        ln.strip() for ln in sec["raw_text"].splitlines() if ln.strip()
    ]
    product_name = products[idx]

    user_id = callback.from_user.id
    await db.add_message_to_history(user_id, "user",
                                    f"Опис продукту: {product_name}")

    await callback.bot.send_chat_action(callback.message.chat.id,
                                        ChatAction.TYPING)
    reply = await generate_cosmetics_reply_ua(
        user_id, f"Опис продукту: {product_name}")
    await db.add_message_to_history(user_id, "assistant", reply)

    md = (f"**_{product_name}_**\n\n"
          f"{reply}\n\n"
          "_✨ Натисніть «Назад», щоб повернутися до списку продуктів_")
    builder = InlineKeyboardBuilder()
    builder.button(text="🔙 Назад", callback_data=f"cosm_sub:{sub_id}")
    builder.adjust(1)

    await callback.message.edit_caption(caption=md,
                                        parse_mode="Markdown",
                                        reply_markup=builder.as_markup())
    await callback.answer()
