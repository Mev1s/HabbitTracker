from app.database.models import UsersOrm
from sqlalchemy import select, update


class UserRepository:
    def __init__(self, session):
        self.session = session

    async def get_all_users(self):
        result = await self.session.execute(select(UsersOrm))
        return result.scalars().all()
