from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from app.core.config import CONTENT_PATH


def load_text_docs(content_path: str):
    loader = DirectoryLoader(content_path, glob="**/*.txt", use_multithreading=True, loader_cls=TextLoader)
    documents = loader.load()
    return documents


def split_docs(documents, chunk_size: int =1000, chunk_overlap: int = 20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    docs = text_splitter.split_documents(documents)
    return docs

TEXT_DOCS = 
