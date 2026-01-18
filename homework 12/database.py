import aiosqlite
from config import DB_NAME


async def create_table():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS quiz_state (
                user_id INTEGER PRIMARY KEY,
                question_index INTEGER DEFAULT 0,
                last_score INTEGER DEFAULT 0,
                last_total INTEGER DEFAULT 0
            )
        """)
        await db.commit()


async def ensure_user(user_id):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            INSERT OR IGNORE INTO quiz_state (user_id)
            VALUES (?)
        """, (user_id,))
        await db.commit()


async def get_quiz_index(user_id):
    await ensure_user(user_id)
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute(
            "SELECT question_index FROM quiz_state WHERE user_id = ?",
            (user_id,)
        ) as cursor:
            row = await cursor.fetchone()
            return row[0]


async def update_quiz_index(user_id, index):
    await ensure_user(user_id)
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "UPDATE quiz_state SET question_index = ? WHERE user_id = ?",
            (index, user_id)
        )
        await db.commit()


async def get_score(user_id):
    await ensure_user(user_id)
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute(
            "SELECT last_score FROM quiz_state WHERE user_id = ?",
            (user_id,)
        ) as cursor:
            row = await cursor.fetchone()
            return row[0]


async def update_score(user_id, score):
    await ensure_user(user_id)
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "UPDATE quiz_state SET last_score = ? WHERE user_id = ?",
            (score, user_id)
        )
        await db.commit()


async def save_result(user_id, score, total):
    await ensure_user(user_id)
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
            UPDATE quiz_state
            SET last_score = ?, last_total = ?, question_index = 0
            WHERE user_id = ?
        """, (score, total, user_id))
        await db.commit()


async def get_stats(limit=10):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("""
            SELECT user_id, last_score, last_total
            FROM quiz_state
            ORDER BY last_score DESC
            LIMIT ?
        """, (limit,)) as cursor:
            return await cursor.fetchall()