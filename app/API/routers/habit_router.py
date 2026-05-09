from typing import List, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ...services.habit_service import habitService
from ..deps.deps import get_db
from ...schemas.habit_schema import (
    HabitResponse as HabitResponseSchema,
    HabitCreate as HabitCreateSchema,
)

habit_router = APIRouter()


@habit_router.get("/all", response_model=List[HabitResponseSchema])
async def get_all(
    db: AsyncSession = Depends(get_db),
) -> List[Dict[HabitResponseSchema, str | int | None]]:
    return await habitService(db).get_all_habits()


@habit_router.get("by_id/{habit_id}", response_model=List[HabitResponseSchema])
async def get_habit_by_id(habit_id: int, db: AsyncSession = Depends(get_db)):
    return await habitService(db).get_habit_by_id(habit_id)


@habit_router.get("/by_title/{title}", response_model=List[HabitCreateSchema])
async def get_habit_by_title(
    title: str, db: AsyncSession = Depends(get_db)
) -> List[Dict[HabitResponseSchema, str | int | None]]:
    return await habitService(db).get_habits_by_title(title)


@habit_router.get("/by_user_id/{user_id}", response_model=List[HabitResponseSchema])
async def get_habits_by_user_id(user_id: int, db: AsyncSession = Depends(get_db)):
    return await habitService(db).get_habits_by_user_id(user_id)


@habit_router.get(
    "/by_user_telegram_id/{telegram_id}", response_model=List[HabitResponseSchema]
)
async def get_habits_by_user_telegram_id(
    telegram_id: int, db: AsyncSession = Depends(get_db)
):
    return await habitService(db).get_habits_by_user_telegram_id(telegram_id)


@habit_router.post("/create", response_model=HabitResponseSchema)
async def create_habit(data: HabitCreateSchema, db: AsyncSession = Depends(get_db)):
    return await habitService(db).create_habit(data)
