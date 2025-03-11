import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s:%(lineno)d #%(levelname)-8s "
    "[%(asctime)s] - %(name)s - %(message)s",
    handlers=[
        logging.FileHandler("bot_logs.log"),  # Log to a file
        logging.StreamHandler()  # Also log to console
    ]
)

logger = logging.getLogger(__name__)