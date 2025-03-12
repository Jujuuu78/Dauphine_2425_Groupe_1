from domain.adapter.generator_controller_adapter import GeneratorControllerAdapter
from domain.service.text_generation_service import TextGenerationService
from domain.service.history_service import HistoryService
from infrastructure.adapter.text_generator_adapter import TextGeneratorAdapter
from infrastructure.adapter.json_history_adapter import JSONHistoryAdapter

def create_generator_rest_adapter():
    text_generator_adapter = TextGeneratorAdapter()
    text_generation_service = TextGenerationService(text_generator_adapter)
    history_adapter = JSONHistoryAdapter(file_path="historic.json")
    history_service = HistoryService(history_adapter)
    generator_controller_adapter = GeneratorControllerAdapter(text_generation_service, history_service)
    return generator_controller_adapter
