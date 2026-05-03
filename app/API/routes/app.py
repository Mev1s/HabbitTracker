from fastapi import FastAPI
from app.API.routes.userRoutes import user_router
from app.API.routes.habitRoutes import habit_router


def create_app():
    app = FastAPI()
    app.include_router(user_router, prefix="/users", tags=["users"])
    app.include_router(habit_router, prefix="/habits", tags=["habits"])
    return app
