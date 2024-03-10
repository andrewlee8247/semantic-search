import os
import logging
import sys
from typing import List

from loguru import logger
from dotenv import find_dotenv
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

from app.core.log import InterceptHandler

API_PREFIX = "/api"
VERSION = "0.0.0"
PARENT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

if fp := find_dotenv(".env"):
    config = Config(fp)  # if using .env file
else:
    config = Config()  # if using environment variables

DEBUG: bool = config("DEBUG", cast=bool, default=False)
OPENAI_API_KEY: str = config("OPENAI_API_KEY", cast=str, default=None)
EMBEDDING_MODEL: str = config("EMBEDDING_MODEL", default="all-MiniLM-L6-v2")
OPENAI_MODEL: str = config("OPENAI_MODEL", default="gpt-3.5-turbo")
PROJECT_NAME: str = config("PROJECT_NAME", default="Semantic Search API")
CONTENT_DIR: str = config("CONTENT_DIR",
                          default=os.path.join(PARENT_DIR, "content"))

ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)

# logging configuration
LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access")

logging.getLogger().handlers = [InterceptHandler()]
for logger_name in LOGGERS:
    logging_logger = logging.getLogger(logger_name)
    logging_logger.handlers = [InterceptHandler(level=LOGGING_LEVEL)]

logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
