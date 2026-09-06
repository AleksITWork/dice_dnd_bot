from aiogram import Bot, Dispatcher
from config import Config
from router import dice_router
from asyncio import run

async def startup():
    config: Config = Config()
    config.load_bot_token()

    bot_token: str = config.get_bot_token()

    bot: Bot = Bot(token=bot_token)
    dispatcher: Dispatcher = Dispatcher()

    dispatcher.include_router(dice_router)

    await dispatcher.start_polling(bot)

if __name__ == "__main__":
    run(startup())