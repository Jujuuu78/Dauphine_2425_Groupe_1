from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from rest.model.chat_request import ChatRequest
from rest.model.single_prompt_response import SinglePromptResponse
from rest.model.conversation_reponse import ConversationResponse

from domain.port.generator_controller_port import GeneratorControllerPort

# Adaptateur REST pour gérer les requêtes HTTP
class GeneratorRestAdapter:
    def __init__(self, controller: GeneratorControllerPort):
        """
        Initialise l'adaptateur avec un contrôleur.
        """
        self.controller = controller

    async def chat(self, request: ChatRequest) -> SinglePromptResponse:
        """
        Gère les requêtes POST à /chat et génère une réponse.
        """
        try:
            response = self.controller.generate_message(request.prompt)
            return SinglePromptResponse(response)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    async def get_all_conversations(self) -> list[str]:
        """
        Récupère toutes les conversations disponibles.
        """
        try:
            return self.controller.get_conversations()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to retrieve conversations: {str(e)}")
    
    async def create_conversation(self) -> str:
        """
        Crée une nouvelle conversation et retourne son identifiant.
        """
        try:
            return self.controller.create_conversation()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to create a new conversation: {str(e)}")
    
    async def get_conversation(self, conversation_guid: str) -> ConversationResponse:
        """
        Récupère l'historique d'une conversation spécifique.
        """
        conversation = self.controller.get_history(conversation_guid)
        if conversation is None:
            raise HTTPException(status_code=404, detail="Conversation not found")
        
        return ConversationResponse(guid=conversation_guid, history=conversation)

    async def generate_message_for_conversation(self, conversation_guid: str, request: ChatRequest) -> ConversationResponse:
        """
        Génère un message pour une conversation spécifique.
        """
        try:
            updated_conversation = self.controller.generate_message_in_conversation(conversation_guid, request.prompt)
            return ConversationResponse(guid=conversation_guid, history=updated_conversation)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    async def clear_conversation(self, conversation_guid: str) -> JSONResponse:
        """
        Efface l'historique d'une conversation spécifique.
        """
        try:
            self.controller.clear_history(conversation_guid)
            return JSONResponse(
                content={"message": f"Conversation {conversation_guid} cleared successfully."},
                status_code=200
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    def get_router(self) -> APIRouter:
        """
        Configure et retourne un routeur FastAPI.
        """
        router = APIRouter()
        router.post("/chat")(self.chat)
        router.get("/conversation")(self.get_all_conversations)
        router.post("/conversation")(self.create_conversation)
        router.get("/conversation/{conversation_guid}")(self.get_conversation)
        router.post("/conversation/{conversation_guid}")(self.generate_message_for_conversation)
        router.delete("/conversation/{conversation_guid}")(self.clear_conversation)
        return router
