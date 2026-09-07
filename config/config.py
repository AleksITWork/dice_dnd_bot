from os import getenv
from utils import singleton

@singleton
class Config:
    _bot_token: str | None = None
    _cube_range: list[tuple[str, int, int]] = [
        ("1-4", 1, 4),
        ("1-6", 1, 6),
        ("1-8", 1, 8),
        ("1-10", 1, 10),
        ("1-12", 1, 12),
        ("1-20", 1, 20),
    ]

    def load_bot_token(self):
        self._bot_token = getenv("BOT_TOKEN")

    def get_bot_token(self) -> str | None:
        return self._bot_token

    def get_cube_range(self) -> list[tuple[str, int, int]]:
        return self._cube_range