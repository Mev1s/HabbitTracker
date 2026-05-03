from fastapi import HTTPException
from sqlalchemy import select
from app.database.models import HabitsOrm


class HabitRepository:
    def __init__(self, session):
        self.session = session

    async def get_all_habits(self):
        result = await self.session.execute(select(HabitsOrm))
        return result.scalars().all()
