from uuid import UUID

from pydantic import BaseModel


class Interaction(BaseModel):
    id:UUID
    prompt:str
    response:str
    