from typing import List

from pydantic import BaseModel


class CohereMessage(BaseModel):
    role: str
    message: str


class HistoryCohere(BaseModel):
    chat_history: List[CohereMessage]
