from fastapi import FastAPI, APIRouter
from app.API.routes.userRoutes import user_router


def create_app():
    app = FastAPI()
    app.include_router(user_router, prefix="/users", tags=["users"])
    return app
