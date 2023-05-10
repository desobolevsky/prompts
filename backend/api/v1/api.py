from fastapi import APIRouter

from api.v1.prompts import router as prompts_router

api_router = APIRouter()
api_router.include_router(prompts_router, prefix='/prompts', tags=["prompts"])
