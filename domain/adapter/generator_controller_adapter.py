from typing import Optional
from uuid import UUID

from domain.model.historic import Historic
from domain.model.interaction import Interaction
from domain.port.generator_controller_port import GeneratorControllerPort
from domain.service.historic_service import HistoricService

from domain.service.text_generation_service import TextGenerationService


class GeneratorControllerAdapter(GeneratorControllerPort):


    def __init__(self,
                text_generation_service: TextGenerationService = None,
                historic_service:HistoricService=None):
        self.text_generation_service = text_generation_service
        self.historic_service = historic_service

    def generate_message(self, prompt: str,id_historic:Optional[UUID]) -> str:
        return self.text_generation_service.get_generated_text(prompt,id_historic)

    def display_historic(self, historic_id: UUID) -> Historic:
        return self.historic_service.get_historic(historic_id)

