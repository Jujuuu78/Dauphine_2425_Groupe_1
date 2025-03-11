from uuid import UUID

from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder
from typing import Optional

from domain.model.historic import Historic


class ChatRequest(BaseModel):
    chat_history_id:Optional[UUID]=None
    prompt: str = Field(title="Prompt", 
                        description="The message to generate a response for", 
                        default="Hello world!")

    def to_dict(self) -> dict:
        return jsonable_encoder(self)