from aiogram import Bot
from config import load_config
from config.logger import logger

config = load_config()


async def notify_admins(bot: Bot):
    config = load_config()
    DEVS = config.tg_bot.DEVID.split(",")

    for DEV in DEVS:
        DEV = DEV.strip()
        if not DEV:
            continue
        try:
            await bot.send_message(DEV, "Bot started!")
        except Exception as e:
            logger.log(
                30, "Can't send start message to DEVID: " + DEV + " Err:" + str(e)
            )
            pass
