from uuid import UUID

from domain.model.historic import Historic
from domain.port.chat_application_port import ChatApplicationPort


class HistoricService:
    def __init__(self, chat_application: ChatApplicationPort):
        self.chat_application = chat_application

    def get_historic(self, historic_id: UUID) -> Historic:
        return self.chat_application.get_historic(historic_id)
