from fastapi import HTTPException

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
            raise HTTPException(status_code=400, detail="User already exists")
        new_user = await repository.user_create(user)
        await self.session.commit()
        await self.session.refresh(new_user)
        return new_user
