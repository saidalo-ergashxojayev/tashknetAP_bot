from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
import logging
from config import load_config
from src.services.database.client import DatabaseManager

config = load_config()
bot = Bot(token=config.tg_bot.BOT_TOKEN,
          default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()
db = DatabaseManager()
