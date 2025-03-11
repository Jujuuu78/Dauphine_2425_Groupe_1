
import os
from dotenv import load_dotenv
import cohere

from domain.model.historic import Historic

load_dotenv()
COHERE_API_KEY = os.environ.get('COHERE_API_KEY')

class CohereTextGenerator():
    def __init__(self):
        self.client = cohere.Client(COHERE_API_KEY)

    def generate_text(self, prompt: str,chat_history:Historic=None) -> str:
        if chat_history:
            response = self.client.chat(
                chat_history=chat_history,
                message=prompt
            )
        else:
            response = self.client.chat(
                message=prompt
            )
        return response.text
