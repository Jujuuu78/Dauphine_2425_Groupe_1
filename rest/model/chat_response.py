from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field


class ChatResponse(BaseModel):
    response: str = Field(title="Response",
                          description="The generated response")

    def to_dict(self) -> dict:
        return jsonable_encoder(self)
