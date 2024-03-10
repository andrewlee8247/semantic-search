from langchain_community.embeddings import SentenceTransformerEmbeddings

from app.core.config import EMBEDDING_MODEL


def initialize_embeddings_model():
    return SentenceTransformerEmbeddings(model_name=EMBEDDING_MODEL)
