from fastapi import FastAPI

from app.API.routers.habit_log_router import habit_log_router
from app.API.routers.user_router import user_router
from app.API.routers.habit_router import habit_router


def create_app():
    app = FastAPI()
    app.include_router(user_router, prefix="/users", tags=["users"])
    app.include_router(habit_router, prefix="/habits", tags=["habits"])
    app.include_router(habit_log_router, prefix="/habit_logs", tags=["habit_logs"])
    return app
