from app.api import server_status, survey_api
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(server_status.router)
api_router.include_router(survey_api.router)
