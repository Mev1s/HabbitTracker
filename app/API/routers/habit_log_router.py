from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..deps.deps import get_db
from ...schemas.habit_logs_schema import HabitLogsResponse as HabitResponseSchema
from ...services.habit_log_service import HabitLogsService


habit_log_router = APIRouter()

@habit_log_router.get("/all", response_model=HabitResponseSchema)
async def get_all_habits_logs(db: AsyncSession = Depends(get_db)):
    return await HabitLogsService(db).get_all_habits_logs()