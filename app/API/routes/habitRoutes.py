from typing import List, Dict

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ...services.habitService import habitService
from ...schemas.habitSchema import (
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
