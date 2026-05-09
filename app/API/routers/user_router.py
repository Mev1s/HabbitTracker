from typing import List, Dict
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, APIRouter

from ...services.user_service import UserService
from ..deps.deps import get_db
from ...schemas.user_schema import (
    UserResponse as UserResponseSchema,
    UserCreate as UserCreateSchema,
)

user_router = APIRouter()


@user_router.get("/all", response_model=List[UserResponseSchema])
async def get_all_users(
    db: AsyncSession = Depends(get_db),
) -> List[Dict[UserResponseSchema, int | datetime]]:
    return await UserService(db).get_all_users()


@user_router.get("/by_id/{user_id}", response_model=UserResponseSchema)
async def get_user_by_id(
    user_id: int, db: AsyncSession = Depends(get_db)
) -> Dict[UserResponseSchema, int | datetime]:
    return await UserService(db).get_user_by_id(user_id)


@user_router.get("/by_tg_id/{telegram_id}", response_model=UserResponseSchema)
async def get_user_by_telegram_id(
    telegram_id, db: AsyncSession = Depends(get_db)
) -> Dict[UserResponseSchema, int | datetime]:
    return await UserService(db).get_user_by_telegram_id(int(telegram_id))


# post


@user_router.post("/create", response_model=UserResponseSchema)
async def user_create(
    user: UserCreateSchema, db: AsyncSession = Depends(get_db)
) -> Dict[UserResponseSchema, int | datetime]:
    return await UserService(db).user_create(user)


# delete

@user_router.delete("/delete/by_id/{user_id}", response_model=UserResponseSchema)
async def user_delete(
    user_id: int, db: AsyncSession = Depends(get_db)
):
    return await UserService(db).user_delete(user_id)
