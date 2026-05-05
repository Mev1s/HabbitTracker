from datetime import datetime
from typing import List, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..deps.deps import get_db
from ...schemas.habit_logs_schema import HabitLogsResponse as HabitLogsResponseSchema
from ...services.habit_log_service import HabitLogsService

habit_log_router = APIRouter()


@habit_log_router.get("/all", response_model=HabitLogsResponseSchema)
async def get_all_habit_logs(
    db: AsyncSession = Depends(get_db),
) -> List[Dict[HabitLogsResponseSchema, int | datetime]]:
    return await HabitLogsService(db).get_all_habit_logs()

@habit_log_router.get("/get_by_id/{habit_log_id}", response_model=HabitLogsResponseSchema)
async def get_habit_logs_by_id(habit_log_id: int, db: AsyncSession = Depends(get_db)):
    return await HabitLogsService(db).get_habit_logs_by_id(habit_log_id)

@habit_log_router.get("/by_telegram_id/{telegram_id}", response_model=List[HabitLogsResponseSchema])
async def get_habit_logs_by_telegram_id(telegram_id: int, db: AsyncSession = Depends(get_db)):
    return await HabitLogsService(db).get_habit_logs_by_telegram_id(telegram_id)
