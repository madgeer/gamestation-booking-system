# Router aggregator
from fastapi import APIRouter
from app.api.v1.endpoints import users, auth, gamestations, bookings, products

api_router = APIRouter()

api_router.include_router(auth.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(gamestations.router, prefix="/gamestations", tags=["gamestations"])
api_router.include_router(bookings.router, prefix="/bookings", tags=["bookings"])
api_router.include_router(products.router, prefix="/products", tags=["products"])