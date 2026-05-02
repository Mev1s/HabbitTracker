from app.database.models import UsersOrm
from sqlalchemy import select, update


class UserRepository:
    def __init__(self, session):
        self.session = session

    async def get_all_users(self):
        result = await self.session.execute(select(UsersOrm))
        return result.scalars().all()

    async def get_user_by_id(self, user_id: int):
        result = await self.session.execute(select(UsersOrm).where(UsersOrm.id == user_id))
        return result.scalars().all()
