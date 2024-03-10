from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from loguru import logger

from app.api.errors.http_error import http_error_handler
from app.api.errors.validation_error import http422_error_handler
from app.api.routes.api import router as api_router
from app.api.routes.health import health_startup_event
from app.utils.loader import initialize_docs_and_db
from app.models.llm import initialize_llm, initialize_semantic_search_chain
from app.models.embeddings import initialize_embeddings_model
from app.core.config import (ALLOWED_HOSTS, API_PREFIX, DEBUG, PROJECT_NAME,
                             VERSION)


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_exception_handler(HTTPException, http_error_handler)
    application.add_exception_handler(RequestValidationError,
                                      http422_error_handler)

    application.include_router(api_router, prefix=API_PREFIX)
    application.add_event_handler("startup", health_startup_event)

    embedding_model = initialize_embeddings_model()
    application.add_event_handler("startup", lambda: initialize_docs_and_db(embedding_model))
    logger.info("Embeddings model and database initialization scheduled.")

    llm_model = initialize_llm()
    application.add_event_handler("startup", lambda: initialize_semantic_search_chain(llm_model))
    logger.info("LLM model initialization scheduled.")

    return application


app = get_application()
