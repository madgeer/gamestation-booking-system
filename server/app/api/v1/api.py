# Router aggregator
from fastapi import APIRouter
from app.api.v1.endpoints import users, auth, gamestations

api_router = APIRouter()

api_router.include_router(auth.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(gamestations.router, prefix="/gamestations", tags=["gamestations"])
