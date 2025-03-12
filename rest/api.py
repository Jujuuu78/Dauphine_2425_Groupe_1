from fastapi import FastAPI

from rest.endpoint.root import router as root_router
from rest.setup import create_generator_rest_adapter

rest_api = FastAPI()
# rest_api = FastAPI(debug=True)  # Active le mode debug
rest_api.include_router(root_router)

generator_rest_adapter = create_generator_rest_adapter()
rest_api.include_router(generator_rest_adapter.get_router())
