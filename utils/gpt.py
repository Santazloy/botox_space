from dotenv import load_dotenv
load_dotenv()

import openai
import db  # для history
from config import OPENAI_API_KEY, SYSTEM_PROMPT_UA
from data.cosmetics_sections import SUBGROUP_DEFINITIONS

# Системний prompt для косметологічного центру (Оксана)
# Визначений у config.py як константа SYSTEM_PROMPT_UA
async def generate_gpt_reply_ua(user_id: int, user_text: str) -> str:
    """
    Генерує загальну відповідь як Оксана, використовуючи історію чатів та SYSTEM_PROMPT_UA.
    """
    openai.api_key = OPENAI_API_KEY
    history = await db.get_message_history(user_id, limit=18)
    messages = [{"role": "system", "content": SYSTEM_PROMPT_UA}]
    messages.extend(history)
    messages.append({"role": "user", "content": user_text})

    try:
        resp = await openai.ChatCompletion.acreate(
            model="gpt-4o",
            messages=messages,
            temperature=0.7
        )
        return resp.choices[0].message.content.strip()
    except Exception:
        return "Вибачте, сервіс GPT наразі недоступний."


# Системний prompt для косметичних брендів
COSMETICS_SYSTEM_PROMPT = (
    "Ти — досвідчений косметолог-консультант з брендів HydroPeptide, Medik8, Image, Is Clinical, "
    "Colorescience, Revitalash, Academie та Histolab. "
    "Ти прекрасно знаєш асортимент кожного бренду з нашого списку, їхні особливості, "
    "головні активні інгредієнти і рекомендації по використанню. "
    "Відповідай виключно про ці бренди і їх продукти. "
    "Якщо питання поза зазначеним списком — ввічливо повідомити про відсутність інформації. "
    "Всі відповіді українською, в дружньому та професійному тоні."
)


async def generate_cosmetics_reply_ua(user_id: int, user_text: str) -> str:
    """
    Генерує експертну відповідь по косметичним брендам,
    підтягує повний перелік продуктів у системний контекст, щоб модель пам’ятала весь асортимент.
    """
    openai.api_key = OPENAI_API_KEY

    # Побудова тексту з усіма підгрупами та продуктами
    products_list = []
    for sec in SUBGROUP_DEFINITIONS:
        # Беремо лише реальні підгрупи (не всі бренди в одному)
        if not sec["id"].endswith("_all"):
            header = f"{sec['emoji']} {sec['title']}"
            body = "\n".join(line.strip() for line in sec["raw_text"].splitlines() if line.strip())
            products_list.append(f"{header}\n{body}\n")

    all_products_text = "\n".join(products_list)

    # Формуємо messages з двома system-повідомленнями:
    messages = [
        {"role": "system", "content": COSMETICS_SYSTEM_PROMPT},
        {"role": "system", "content": "Повний асортимент продуктів:\n" + all_products_text}
    ]

    # Додаємо user-запит
    await db.add_message_to_history(user_id, "user", user_text)
    messages.append({"role": "user", "content": user_text})

    try:
        resp = await openai.ChatCompletion.acreate(
            model="gpt-4o",
            messages=messages,
            temperature=0.3,
            max_tokens=700
        )
        answer = resp.choices[0].message.content.strip()
        await db.add_message_to_history(user_id, "assistant", answer)
        return answer
    except Exception:
        return "Вибачте, косметологічний сервіс GPT наразі недоступний."
