from dataclasses import dataclass
from dotenv import load_dotenv
from .base import getenv


@dataclass
class TelegramBotConfig:
    BOT_URL: str
    SPECIAL_CHANNEL_URL: str
    REQUIRED_REFERRAL_COUNT: int
    REQUIRED_CHANNELS: str
    PHOTO_ID: str
    BOT_TOKEN: str
    ADMINS: str
    DEVID: str


# @dataclass
# class PostgresConfig:
#     DBUSER: str
#     DBPASSWORD: str
#     HOST: str
#     PORT: int
#     DBNAME: str


@dataclass
class Config:
    tg_bot: TelegramBotConfig
    # postgres: PostgresConfig


def load_config() -> Config:
    load_dotenv(override=True)

    return Config(
        tg_bot=TelegramBotConfig(
            BOT_TOKEN=getenv("BOT_TOKEN"),
            ADMINS=getenv("ADMINS"),
            DEVID=getenv("DEVID"),
            BOT_URL=getenv("BOT_URL"),
            SPECIAL_CHANNEL_URL=getenv("SPECIAL_CHANNEL_URL"),
            REQUIRED_REFERRAL_COUNT=getenv("REQUIRED_REFERRAL_COUNT", int),
            PHOTO_ID=getenv("PHOTO_ID"),
            REQUIRED_CHANNELS=getenv("REQUIRED_CHANNELS"),
        ),
        # postgres=PostgresConfig(
        #     DBUSER=getenv("DBUSER"),
        #     DBPASSWORD=getenv("DBPASSWORD"),
        #     HOST=getenv("HOST"),
        #     PORT=getenv("PORT"),
        #     DBNAME=getenv("DBNAME"),
        # )
    )
