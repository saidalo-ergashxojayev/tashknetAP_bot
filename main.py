import asyncio
from loader import bot, dp, db
from config.logger import logger
from src.utils.telegram import notify_admins
from src.handlers import start, menu, admin
from src.middleware.subscription import SubscriptionMiddleware


async def main():
    logger.info("Starting bot")
    await notify_admins(bot)
    db.connect()
    db.create_table()

    dp.message.middleware(SubscriptionMiddleware(db, bot))

    dp.include_router(admin.router)
    dp.include_router(start.router)
    dp.include_router(menu.router)

    await bot.delete_webhook(drop_pending_updates=False)
    await dp.start_polling(bot)
    db.disconnect()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
