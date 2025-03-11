import os
import uuid
from dataclasses import dataclass
from typing import Optional
from uuid import UUID

from dotenv import load_dotenv
import cohere

from domain.model.historic import Historic
from domain.model.interaction import Interaction
from domain.port.chat_application_port import ChatApplicationPort
from infrastructure.repository.historic_repository import HistoricRepository

from infrastructure.text_generator.cohere_text_generator import CohereTextGenerator

load_dotenv()
COHERE_API_KEY = os.environ.get('COHERE_API_KEY')
PATH_JSON_FILE = "./infrastructure/repository/historic_data.json"

@dataclass
class ChatApplicationAdapter(ChatApplicationPort):
    cohere_text_generator: CohereTextGenerator = CohereTextGenerator()
    historic_repository:HistoricRepository=HistoricRepository(PATH_JSON_FILE)

    def get_generated_text(self, prompt: str,historic:Historic=None) -> str:
        generate_text= self.cohere_text_generator.generate_text(prompt=prompt,chat_history=historic)
        return generate_text

    def get_historic(self, id_historic: UUID) -> Optional[Historic]:
        return self.historic_repository.get(id_historic)

    def save_historic(self, interaction: Interaction, id_historic: UUID=None):
        return self.historic_repository.save(interaction, id_historic)