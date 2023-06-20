from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import token


bot = Bot(token=token)
dp = Dispatcher(bot, storage=MemoryStorage())