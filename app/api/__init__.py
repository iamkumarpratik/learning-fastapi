from app.api import server_status
from fastapi import APIRouter

api_router = APIRouter()

api_router.include_router(server_status.router)
