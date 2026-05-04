from sqlalchemy import select, update

from app.database.models import UsersOrm


class UserRepository:
    def __init__(self, session):
        self.session = session

    async def get_all_users(self):
        result = await self.session.execute(select(UsersOrm))
        return result.scalars().all()

    async def get_user_by_id(self, user_id: int):
        result = await self.session.execute(
            select(UsersOrm).where(UsersOrm.id == user_id)
        )
        return result.scalars().one_or_none()

    async def get_user_by_telegram_id(self, telegram_id: int):
        result = await self.session.execute(
            select(UsersOrm).where(UsersOrm.telegram_id == telegram_id)
        )
        return result.scalars().one_or_none()

    async def user_create(self, user: UsersOrm):
        new_user = UsersOrm(**user.model_dump())
        self.session.add(new_user)
        return new_user
