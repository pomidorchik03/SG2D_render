import asyncio
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
import json

import user_commands
import generator_img


TOKEN = "6619686897:AAEnRkvqAwA4JXyBMpX-MYts660nIXWtAEA"

bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()


@dp.message(Command(commands=['joskoegayporno']))
async def offBot(message: Message, bot: Bot) -> None:
    print("Бот остановлен")
    await dp.stop_polling()


async def main():

    dp.include_routers(
        user_commands.router,
        generator_img.router
    )

    print("бот запущен")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
