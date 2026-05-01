from fastapi import FastAPI, APIRouter
from app.API.routes.user_routes import user_router

def create_app():
    app = FastAPI()
    app.include_router(user_router, prefix="/users")
    return app

