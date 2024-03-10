import logging
import sys
from typing import List
import boto3
import json
import base64

from loguru import logger
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

from app.core.log import InterceptHandler

API_PREFIX = "/api"
VERSION = "0.0.0"

config = Config(".env")

DEBUG: bool = config("DEBUG", cast=bool, default=False)
OPENAI_API_KEY: str = config("OPENAI_API_KEY", cast=str, default=None)
EMBEDDING_MODEL: str = config("EMBEDDING_MODEL",
                              default="all-MiniLM-L6-v2")
OPENAI_MODEL: str = config("OPENAI_MODEL", default="gpt-3.5-turbo")
PROJECT_NAME: str = config("PROJECT_NAME",
                           default="Semantic Search API")
CONTENT_PATH: str = config("CONTENT_PATH", default="../../content") # TODO: change to s3 bucket

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