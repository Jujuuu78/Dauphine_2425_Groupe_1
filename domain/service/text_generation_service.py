import uuid
from uuid import UUID

from domain.model.historic import Historic
from domain.model.interaction import Interaction
from domain.port.chat_application_port import ChatApplicationPort


class TextGenerationService:
    def __init__(self, chat_application: ChatApplicationPort):
        self.chat_application = chat_application

    def get_generated_text(self, prompt: str,id_historic:UUID=None) -> str:
        historic=self.chat_application.get_historic(id_historic)
        generate_message= self.chat_application.get_generated_text(prompt,historic)
        interaction=Interaction(
            id=uuid.uuid4(),
            prompt=prompt,
            response=generate_message,
        )
        print(interaction)
        self.chat_application.save_historic(interaction,id_historic)
        return generate_message