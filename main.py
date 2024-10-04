import logging
import sys
from asyncio import run

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand
from decouple import config

from functions import get_user_info, shutdown_answer, startup_answer

BOT_TOKEN = config("BOT_TOKEN")
dp = Dispatcher()


async def start():
    dp.startup.register(startup_answer)
    dp.message.register(get_user_info)
    dp.shutdown.register(shutdown_answer)
    bot = Bot(token=BOT_TOKEN,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.set_my_commands([
        BotCommand(command="/start", description="Botni ishga tushirish"),
        BotCommand(command='/help', description="Yordam!")
    ])
    await dp.start_polling(bot, polling_timeout=1)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    run(start())
