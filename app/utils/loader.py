from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

from app.core.config import CONTENT_DIR
from app.models.embeddings import initialize_embeddings_model


def load_text_docs(content_path: str):
    loader = DirectoryLoader(content_path,
                             glob="**/*.txt",
                             use_multithreading=True,
                             loader_cls=TextLoader)
    return loader.load()


def split_docs(documents, chunk_size: int = 1000, chunk_overlap: int = 20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,
                                                   chunk_overlap=chunk_overlap)
    return text_splitter.split_documents(documents)


def initialize_docs_and_db(embeddings_model):
    docs = split_docs(load_text_docs(CONTENT_DIR))
    return Chroma.from_documents(docs, embeddings_model)


db = initialize_docs_and_db(initialize_embeddings_model())
