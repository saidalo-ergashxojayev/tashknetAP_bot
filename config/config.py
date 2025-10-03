from dataclasses import dataclass
from dotenv import load_dotenv
from .base import getenv


@dataclass
class TelegramBotConfig:
    BOT_TOKEN: str
    ADMINS: str
    DEVID: str


@dataclass
class APIConfig:
    OPEN_WEATHER_APPID: str


@dataclass
class Config:
    tg_bot: TelegramBotConfig
    api: APIConfig


def load_config() -> Config:
    load_dotenv(override=True)

    return Config(
        tg_bot=TelegramBotConfig(
            BOT_TOKEN=getenv("BOT_TOKEN"),
            ADMINS=getenv("ADMINS"),
            DEVID=getenv("DEVID"),
        ),
        api=APIConfig(
            OPEN_WEATHER_APPID=getenv("OPEN_WEATHER_API"),
        ),
    )
