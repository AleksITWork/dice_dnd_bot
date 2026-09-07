from logging import Logger, getLogger
from aiogram import Bot, Dispatcher
from config import Config
from router import dice_router
from asyncio import run
from utils import setup_logging

setup_logging(level="INFO")
logger: Logger = getLogger(__name__)

async def startup():
    logger.info("Initializing settings...")

    config: Config = Config()
    config.load_bot_token()

    bot_token: str = config.get_bot_token()

    if bot_token is None:
        logger.critical("Bot token not found!")
        return

    bot: Bot = Bot(token=bot_token)
    dispatcher: Dispatcher = Dispatcher()

    dispatcher.include_router(dice_router)

    logger.info("Bot successfully started!")

    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    try:
        run(startup())
    except KeyboardInterrupt:
        logger.info("Bot stopped by user!")
    except Exception as e:
        logger.critical(f"Critical error: {e}!", exc_info=True)