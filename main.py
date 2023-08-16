from aiogram import Bot, Dispatcher
from src.handlers import route
from aiogram.fsm.storage.memory import MemoryStorage

import asyncio

bot = Bot(token='6477814839:AAH-oy1vB9toWF2r7CmvVdUV3yjxkUERigQ')
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(route)

async def main():
  await bot.delete_webhook(drop_pending_updates=True)
  await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped!')