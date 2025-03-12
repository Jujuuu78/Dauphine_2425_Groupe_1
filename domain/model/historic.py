from typing import List
from uuid import UUID

from pydantic import BaseModel

from domain.model.interaction import Interaction


class Historic(BaseModel):
    id: UUID
    interactions:List[Interaction]

    def model_dump(self):
        return {
            "id": str(self.id),  # Convertir UUID en string pour compatibilité JSON
            "interactions": [interaction.model_dump() for interaction in self.interactions]
        }