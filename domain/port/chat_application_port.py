from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID

from domain.model.historic import Historic
from domain.model.interaction import Interaction


class ChatApplicationPort(ABC):
    @abstractmethod
    def get_generated_text(self, prompt: str,historic:Historic=None) -> str:
        pass

    @abstractmethod
    def get_historic(self, id_historic: UUID) -> Optional[Historic]:
        pass

    @abstractmethod
    def save_historic(self, interaction: Interaction,id_historic:UUID):
        pass
