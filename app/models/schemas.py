from pydantic import BaseModel


class QueryReturn(BaseModel):
    answer: str
