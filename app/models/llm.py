from langchain_openai import ChatOpenAI
from langchain.chains.question_answering import load_qa_chain

from app.core.config import OPENAI_API_KEY, OPENAI_MODEL


def initialize_llm():
    return ChatOpenAI(model_name=OPENAI_MODEL, openai_api_key=OPENAI_API_KEY)


def initialize_semantic_search_chain(llm):
    return load_qa_chain(llm, chain_type="stuff", verbose=True)


llm_model = initialize_llm()
chain = initialize_semantic_search_chain(llm_model)
