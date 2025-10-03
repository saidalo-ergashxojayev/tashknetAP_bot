import asyncio
from aiogram import types
from loader import bot, dp
from config.logger import logger
from src.utils.telegram import notify_admins
from src.handlers import start, menu, check_live, get_historical_data
from src.helper.tashkent_radius_check import is_in_tashkent


async def main():
    logger.info("Starting bot")
    await notify_admins(bot)

    commands = [
        types.BotCommand(command="/start", description="Start the bot"),
    ]

    await bot.set_my_commands(commands)

    dp.include_router(start.router)
    dp.include_router(menu.router)
    dp.include_router(check_live.router)
    dp.include_router(get_historical_data.router)
    

    await bot.delete_webhook(drop_pending_updates=False)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
