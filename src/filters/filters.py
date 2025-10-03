from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from config import load_config
from config.consts import DISTRICTS
config = load_config()


class AdminFilter(BaseFilter):
    def __init__(self) -> None:
        admins = config.tg_bot.ADMINS.split(",")
        self.admin_ids = admins

    async def __call__(self, message: Message) -> bool:
        return str(message.from_user.id) in self.admin_ids


class DistrictFilter(BaseFilter):
    def __init__(self) -> None:
        self.districts = DISTRICTS

    async def __call__(self, message: Message) -> bool:
        return message.text in self.districts.values()