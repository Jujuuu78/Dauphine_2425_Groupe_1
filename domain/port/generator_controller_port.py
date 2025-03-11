from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from domain.model.historic import Historic
from domain.model.interaction import Interaction


class GeneratorControllerPort(ABC):
    @abstractmethod
    def generate_message(self, prompt: str,id_historic:Optional[UUID]) -> str:
        pass

    @abstractmethod
    def display_historic(self, id:UUID) -> Historic:
        pass

