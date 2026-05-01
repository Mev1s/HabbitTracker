from ...repository.user import UserRepository
from ...schemas.user import UserResponse as UserResponseSchema, UserCreate as UserCreateSchema
from ..deps.deps import get_db
from fastapi import Depends, APIRouter
from typing import List, Dict
from sqlalchemy.ext.asyncio import AsyncSession

user_router = APIRouter()

@user_router.get("/users", response_model=List[UserResponseSchema])
async def get_all_users(db: AsyncSession = Depends(get_db)) -> UserResponseSchema:
    return await UserRepository(db).get_all_users()