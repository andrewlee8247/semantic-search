from fastapi import APIRouter, status
from loguru import logger

from app.models.schemas import QueryReturn
from app.utils.loader import db
from app.models.llm import chain


router = APIRouter()


@router.get(
    path="",
    response_model=QueryReturn,
    name="Semantic Document Search",
    description="""
    query: Prompt to search for relevant documents
    """,
    status_code=status.HTTP_200_OK,
)
async def semantic_search(query: str,):
    matching_docs = db.similarity_search(query)
    logger.info(f"Matching documents: {matching_docs}")
    answer = chain.run(input_documents=matching_docs, question=query)
    return {"answer": answer}
