from domain.model.historic import Historic
from infrastructure.models.history_cohere import HistoryCohere, CohereMessage


class CohereMapper:
    @staticmethod
    def map_historic_to_cohere(historic: Historic) -> HistoryCohere:
        """
        Convertit un objet Historic en un objet HistoryCohere compatible avec l'API Cohere.

        :param historic: Objet Historic contenant la liste des interactions
        :return: Objet HistoryCohere formaté pour Cohere
        """
        messages = []

        for interaction in historic.interactions:
            messages.append(CohereMessage(role="USER", message=interaction.prompt))
            messages.append(CohereMessage(role="CHATBOT", message=interaction.response))

        return HistoryCohere(chat_history=messages)
