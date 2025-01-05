from aiogram import BaseMiddleware, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.exceptions import TelegramBadRequest
from config import load_config
from typing import Callable, Dict, Any, Awaitable
from loader import DatabaseManager
from config.logger import logger

config = load_config()

REQUIRED_CHANNELS = config.tg_bot.REQUIRED_CHANNELS.split(",")


class SubscriptionMiddleware(BaseMiddleware):
    def __init__(self, db: DatabaseManager, bot: Bot):
        self.db = db
        self.bot = bot
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[Message | CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: Message | CallbackQuery,
        data: Dict[str, Any],
    ) -> Any:
        user_id = None
        if isinstance(event, Message):
            user_id = event.from_user.id
        logger.log(20, "USER: "+str(user_id)+", "+event.from_user.full_name)
        if user_id:
            try:
                if isinstance(event, Message) and event.text.startswith("/start"):
                    command_args = event.text.split(" ", maxsplit=1)
                    referrer_id = command_args[1] if len(
                        command_args) > 1 else None

                    state = data.get("state")
                    if state and referrer_id:
                        await state.update_data(referrer_id=referrer_id)

                unsubscribed_channels = []

                for channel in REQUIRED_CHANNELS:
                    try:
                        chat_member = await self.bot.get_chat_member(chat_id=f"{channel}", user_id=user_id)
                        if chat_member.status not in ("member", "administrator", "creator"):
                            unsubscribed_channels.append(channel)
                    except TelegramBadRequest as e:
                        logger.log(30, f"Error checking channel {channel}: {e}")
                        continue  # If we fail to get the member status, continue with the next channel

                # If user is not subscribed to any channels, show the subscribe buttons
                if unsubscribed_channels:
                    subscribe_keyboard = InlineKeyboardMarkup(
                        inline_keyboard=[])

                    for i, channel in enumerate(unsubscribed_channels, start=1):
                        chat = await self.bot.get_chat(chat_id=f"{channel}")
                        link = chat.invite_link
                        
                        subscribe_keyboard.inline_keyboard.append(
                            [
                                InlineKeyboardButton(
                                    text=f"📢 {i}-kanalga obuna bo'lish",
                                    url=link
                                )
                            ]
                        )

                    subscribe_keyboard.inline_keyboard.append(
                        [
                            InlineKeyboardButton(
                                text="✅ Obunani Tasdiqlash",
                                callback_data="verify_subscription"
                            )
                        ]
                    )

                    if isinstance(event, Message):
                        await self.bot.send_message(
                            chat_id=user_id,
                            text="Botdan foydalanish uchun quyidagi kanallarda obuna bo'lishingiz kerak. 👇",
                            reply_markup=subscribe_keyboard,
                            parse_mode="HTML"
                        )

                    return

            except Exception as e:
                logger.log(50, f"Error in SubscriptionMiddleware: {e}")

        return await handler(event, data)
