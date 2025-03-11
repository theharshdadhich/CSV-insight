from pydantic import BaseModel

from pydantic_ai import Agent

class Response(BaseModel):
    response : str
    