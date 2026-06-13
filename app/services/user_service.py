from fastapi import HTTPException
from sqlalchemy.sql.functions import user

from app import repository
from app.repository.user_repository import UserRepository
from app.schemas.user_schema import UserCreate


class UserService:
    def __init__(self, session):
        self.session = session

    async def get_all_users(self):
        return await UserRepository(self.session).get_all_users()

    async def get_user_by_id(self, user_id: int):
        result = await UserRepository(self.session).get_user_by_id(user_id)
        if not result:
            raise HTTPException(status_code=404, detail="User not found")
        return result

    async def get_user_by_telegram_id(self, telegram_id: int):
        result = await UserRepository(self.session).get_user_by_telegram_id(telegram_id)
        if not result:
            raise HTTPException(status_code=404, detail="User not found")
        return result

    async def user_create(self, user: UserCreate):
        repository = UserRepository(self.session)
        result_user_by_telegram_id = await repository.get_user_by_telegram_id(
            telegram_id=user.telegram_id
        )
        if result_user_by_telegram_id:
            raise HTTPException(status_code=409, detail="User already exists")
        new_user = await repository.user_create(user)
        await self.session.commit()
        await self.session.refresh(new_user)
        return new_user

    async def user_delete(self, user_id: int):
        user = await UserRepository(self.session).get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        user = await UserRepository(self.session).user_delete(user)
        await self.session.commit()
        self.session.refresh(user)
        return user

    async def user_update(self, user_data, user_id: int):
        user_get = await UserRepository(self.session).get_user_by_id(user_id)
        if not user_get:
            raise HTTPException(status_code=404, detail="User not found")

        user_data = user_data.model_dump(exclude_unset=True)
        if not user_data:
            raise HTTPException(status_code=400, detail="user data is null")

        result = await UserRepository(self.session).user_update(user_data, user_id)
        await self.session.commit()
        return result
