# db.py
import os
import logging
import asyncpg
from typing import List, Dict, Optional
from urllib.parse import urlparse, urlunparse # Для безопасного логирования DATABASE_URL

db_pool: Optional[asyncpg.Pool] = None

async def init_db_pool():
    global db_pool

    original_conn_str_from_env = os.getenv("DATABASE_URL")
    conn_str_to_use = original_conn_str_from_env
    dsn_for_logging = ""

    if not conn_str_to_use:
        # DATABASE_URL не установлена, конструируем строку из PG* переменных
        PGHOST = os.getenv("PGHOST", "db.ddsjsfqpixkuhnmqljst.supabase.co") # Замените на ваш PGHOST по умолчанию, если нужно
        PGPORT = os.getenv("PGPORT", "5432")
        PGUSER = os.getenv("PGUSER", "postgres") # Замените на ваш PGUSER по умолчанию
        # PGPASSWORD определяется здесь и используется для формирования conn_str_to_use
        PGPASSWORD_val = os.getenv("PGPASSWORD", "") 
        PGDATABASE = os.getenv("PGDATABASE", "postgres") # Замените на ваш PGDATABASE по умолчанию

        if not PGPASSWORD_val and PGUSER != "postgres": # Для стандартного пользователя postgres пароль часто не требуется локально, но для других - да
            logging.warning(
                "Переменная окружения PGPASSWORD не установлена или пуста. "
                "Соединение может не удасться, если пароль обязателен."
            )

        conn_str_to_use = f"postgresql://{PGUSER}:{PGPASSWORD_val}@{PGHOST}:{PGPORT}/{PGDATABASE}?sslmode=require"
        # Для логирования маскируем пароль в сконструированной строке
        dsn_for_logging = f"postgresql://{PGUSER}:<password_masked>@{PGHOST}:{PGPORT}/{PGDATABASE}?sslmode=require"
        logging.info(f"DATABASE_URL не установлена. Используется сконструированный DSN.")
    else:
        # DATABASE_URL установлена
        logging.info(f"Используется DATABASE_URL из переменных окружения.")
        # Попытка замаскировать пароль в DATABASE_URL для безопасного логирования
        try:
            parsed_url = urlparse(conn_str_to_use)
            if parsed_url.password:
                safe_netloc = parsed_url.username or ""
                safe_netloc += ":<password_masked>"
                if parsed_url.hostname:
                    safe_netloc += f"@{parsed_url.hostname}"
                if parsed_url.port:
                    safe_netloc += f":{parsed_url.port}"

                url_parts = list(parsed_url)
                url_parts[1] = safe_netloc # Заменяем netloc на безопасную версию
                dsn_for_logging = urlunparse(url_parts)
            else:
                dsn_for_logging = conn_str_to_use # Пароля нет в URL
        except Exception as e:
            logging.warning(f"Не удалось замаскировать пароль в DATABASE_URL для логирования: {e}. Логирование полного URL может быть небезопасным.")
            dsn_for_logging = "DSN from DATABASE_URL (маскировка пароля не удалась или не требуется)"


    logging.info(f"Попытка создать пул соединений с DSN: {dsn_for_logging}")

    if not conn_str_to_use:
        logging.error("Строка подключения к БД пуста. Пул не будет создан.")
        db_pool = None
        raise ValueError("Строка подключения к БД не может быть пустой.")

    try:
        db_pool = await asyncpg.create_pool(dsn=conn_str_to_use, min_size=1, max_size=10)
        logging.info("Пул соединений с PostgreSQL успешно создан.")
    except Exception as e:
        logging.error(f"Ошибка при создании пула соединений с DSN '{dsn_for_logging}': {e}")
        db_pool = None 
        raise

async def create_tables():
    if not db_pool:
        raise RuntimeError("db_pool is None! Сначала вызовите init_db_pool().")

    async with db_pool.acquire() as conn:
        await conn.execute("""
            CREATE TABLE IF NOT EXISTS message_history (
                id SERIAL PRIMARY KEY,
                user_id BIGINT NOT NULL,
                role TEXT NOT NULL, CHECK (role IN ('user', 'assistant', 'system')),
                content TEXT NOT NULL,
                timestamp TIMESTAMPTZ DEFAULT NOW()
            )
        """)
        await conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_message_history_user_timestamp 
            ON message_history (user_id, timestamp DESC);
        """)
        logging.info("Таблица 'message_history' создана/проверена.")

async def add_message_to_history(user_id: int, role: str, content: str):
    if not db_pool:
        logging.error("db_pool is None in add_message_to_history. Сообщение не сохранено.")
        return

    async with db_pool.acquire() as conn:
        await conn.execute(
            "INSERT INTO message_history (user_id, role, content) VALUES ($1, $2, $3)",
            user_id, role, content
        )
        await conn.execute(
            """
            DELETE FROM message_history
            WHERE id IN (
                SELECT id FROM message_history
                WHERE user_id = $1
                ORDER BY timestamp ASC
                LIMIT GREATEST(0, (SELECT COUNT(*) FROM message_history WHERE user_id = $1) - 20)
            )
            """,
            user_id
        )

async def get_message_history(user_id: int, limit: int = 20) -> List[Dict[str, str]]:
    if not db_pool:
        logging.error("db_pool is None in get_message_history. История не получена.")
        return []

    async with db_pool.acquire() as conn:
        rows = await conn.fetch(
            """
            SELECT role, content FROM (
                SELECT role, content, timestamp
                FROM message_history
                WHERE user_id = $1
                ORDER BY timestamp DESC
                LIMIT $2
            ) AS recent_history
            ORDER BY timestamp ASC;
            """,
            user_id, limit
        )
        return [{'role': row['role'], 'content': row['content']} for row in rows]

async def close_db_pool():
    global db_pool
    if db_pool:
        await db_pool.close()
        db_pool = None
        logging.info("Пул соединений PostgreSQL закрыт.")