from fastapi import FastAPI
from app.api import api_router


def create_app():

    fast_app = FastAPI()
    fast_app.include_router(api_router)
    return fast_app
