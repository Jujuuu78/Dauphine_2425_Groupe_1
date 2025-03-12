import os

import cohere
from dotenv import load_dotenv

from domain.model.historic import Historic
from infrastructure.mapper.mapper_cohere import CohereMapper

load_dotenv()
COHERE_API_KEY = os.environ.get('COHERE_API_KEY')


class CohereTextGenerator():
    def __init__(self):
        self.client = cohere.Client(COHERE_API_KEY)

    def generate_text(self, prompt: str, chat_history: Historic = None) -> str:
        history = CohereMapper.map_historic_to_cohere(chat_history).chat_history if chat_history else None

        response = self.client.chat(
            message=prompt,
            chat_history=history
        )
        return response.text
