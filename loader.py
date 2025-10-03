from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
from config import load_config
from src.helper.open_weather import OpenWeatherRequest
from config.consts import OPEN_WEATHER_API_URL

config = load_config()
bot = Bot(token=config.tg_bot.BOT_TOKEN,
          default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()
ow = OpenWeatherRequest(api_key=config.api.OPEN_WEATHER_APPID, base_url=OPEN_WEATHER_API_URL)
