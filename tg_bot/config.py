import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis

from tg_bot.handlers.commands import router as commands_router


class Config:
    BOT_TOKEN = os.getenv('BOT_TOKEN')


bot = Bot(Config.BOT_TOKEN)

storage = RedisStorage(Redis(), state_ttl=5400, data_ttl=5400)
dispatcher = Dispatcher(storage=storage)
dispatcher.include_router(commands_router)
