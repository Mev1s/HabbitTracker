from typing import List, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ...services.habit_service import habitService
from ...schemas.habit_schema import (
    HabitResponse as HabitResponseSchema,
    HabitCreate as HabitCreateSchema,
)
from ..deps.deps import get_db

habit_router = APIRouter()


@habit_router.get("/all", response_model=HabitResponseSchema)
async def get_all(
    db: AsyncSession = Depends(get_db),
) -> List[Dict[HabitResponseSchema, str | int | None]]:
    return await habitService(db).get_all_habits()


@habit_router.get("/by_title/{title}", response_model=HabitCreateSchema)
async def get_habit_by_title(
    title: str, db: AsyncSession = Depends(get_db)
) -> List[Dict[HabitResponseSchema, str | int | None]]:
    return await habitService(db).get_habits_by_title(title)


@habit_router.get("/by_user_id/{user_id}", response_model=HabitResponseSchema)
async def get_habits_by_user_id(user_id: int, db: AsyncSession = Depends(get_db)):
    return await habitService(db).get_habits_by_user_id(user_id)


@habit_router.get(
    "/by_user_telegram_id/{telegram_id}", response_model=HabitResponseSchema
)
async def get_habits_by_user_telegram_id(
    telegram_id: int, db: AsyncSession = Depends(get_db)
):
    return await habitService(db).get_habits_by_user_telegram_id(telegram_id)
