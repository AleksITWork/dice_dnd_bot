from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from random import randint
from config import Config

def _build_card(idx: int, title: str, min_number: int, max_number: int) -> InlineQueryResultArticle:
    number = randint(min_number, max_number)
    message_text: str = f"The {max_number}-granular cube was abandoned.\nYour result: {number}!"
    if number == min_number:
        message_text += "\nCritical failure! To be in trouble..."
    elif number == max_number:
        message_text += "\nCritical luck! it's real?"

    return InlineQueryResultArticle(
        id=str(idx),
        title=f"🎲 | Interval: {title}",
        description=f"Get random number in interval [{min_number};{max_number}]",
        input_message_content=InputTextMessageContent(
            message_text=message_text
        )
    )

dice_router: Router = Router()
config: Config = Config()

@dice_router.inline_query()
async def handle_inline(query: InlineQuery):
    results: list[InlineQueryResultArticle] = [
        _build_card(i, title, min_number, max_number)
        for i, (title, min_number, max_number) in enumerate(config.get_cube_range())
    ]

    await query.answer(
        results=results,
        cache_time=1,
        is_personal=True,
    )