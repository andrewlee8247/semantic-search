from fastapi import APIRouter, status
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain
from loguru import logger

from app.models import schemas
from app.core.config import OPENAI_API_KEY, CONTENT_DIR, EMBEDDING_MODEL, OPENAI_MODEL
from app.utils.loader import split_docs, load_text_docs


embeddings = SentenceTransformerEmbeddings(model_name=EMBEDDING_MODEL)
docs = split_docs(load_text_docs(CONTENT_DIR))

db = Chroma.from_documents(docs, embeddings)
llm = ChatOpenAI(model_name=OPENAI_MODEL, openai_api_key=OPENAI_API_KEY)
chain = load_qa_chain(llm, chain_type="stuff", verbose=True)

router = APIRouter()


@router.get(
    path="",
    response_model=schemas.QueryReturn,
    name="Semantic Document Search",
    description="""
    query: Prompt to search for relevant documents
    """,
    status_code=status.HTTP_200_OK,
)
async def semantic_search(query: str):
    matching_docs = db.similarity_search(query)
    logger.info(f"Matching documents: {matching_docs}")
    answer = chain.run(input_documents=matching_docs, question=query)
    return {"answer": answer}
