from bot import bot, dp
from database import create_table
import handlers
import asyncio

async def main():
    await create_table()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())