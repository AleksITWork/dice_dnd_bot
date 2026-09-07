import logging
from logging import Formatter, Logger
from pathlib import Path
import sys

def setup_logging(level: str = "INFO"):
    """
    Функция настройки логирования
    """

    formatter: Formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)-8s | %(name)-20s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    root_logger: Logger = logging.getLogger("root")
    level = getattr(logging, level.upper())
    root_logger.setLevel(level)

    root_logger.handlers.clear()

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    root_logger.addHandler(console_handler)

    Path("logs").mkdir(parents=True, exist_ok=True)
    file_handler = logging.FileHandler(f"logs/bot.log", encoding="utf-8")
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)