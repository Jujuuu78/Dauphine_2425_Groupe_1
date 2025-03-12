from uuid import UUID

from pydantic import BaseModel


class Interaction(BaseModel):
    id:UUID
    prompt:str
    response:str

    def model_dump(self):
        return {
            "id": str(self.id),  # Convertir UUID en string pour éviter les erreurs JSON
            "prompt": self.prompt,
            "response": self.response
        }