from datetime import datetime

from sqlalchemy import select

from app.database.models import HabitsOrm, UsersOrm
from ..schemas.habit_schema import HabitCreate


class HabitRepository:
    def __init__(self, session):
        self.session = session

    async def get_all_habits(self):
        result = await self.session.execute(select(HabitsOrm))
        return result.scalars().all()

    async def get_habit_by_id(self, habit_id: int):
        result = await self.session.execute(
            select(HabitsOrm).where(HabitsOrm.id == habit_id)
        )
        return result.scalars().all()

    async def get_habits_by_title(self, title: str):
        result = await self.session.execute(
            select(HabitsOrm).where(HabitsOrm.title == title)
        )
        return result.scalars().all()

    async def get_habits_by_user_id(self, user_id: int):
        result = await self.session.execute(
            select(HabitsOrm).join(UsersOrm).where(HabitsOrm.user_id == UsersOrm.id)
        )
        return result.scalars().all()

    async def create_habit(self, data: HabitCreate):
        new_habit = HabitsOrm(**data.model_dump())
        self.session.add(new_habit)
        return new_habit
