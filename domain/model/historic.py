from typing import List
from uuid import UUID

from pydantic import BaseModel

from domain.model.interaction import Interaction


class Historic(BaseModel):
    id: UUID
    interactions:List[Interaction]