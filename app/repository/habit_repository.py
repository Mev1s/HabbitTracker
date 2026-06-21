from datetime import datetime

from sqlalchemy import select, update

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
        return result.scalars().one_or_none()

    async def get_habits_by_title(self, title: str):
        result = await self.session.execute(
            select(HabitsOrm).where(HabitsOrm.title == title)
        )
        return result.scalars().one_or_none()

    async def get_habits_by_user_id(self, user_id: int):
        result = await self.session.execute(
            select(HabitsOrm).join(UsersOrm).where(HabitsOrm.user_id == UsersOrm.id)
        )
        return result.scalars().all()

    async def create_habit(self, data: HabitCreate):
        new_habit = HabitsOrm(**data.model_dump())
        self.session.add(new_habit)
        return new_habit

    async def delete_habit(self, habit):
        await self.session.delete(habit)
        return habit

    async def update_habit(self, id: int, data):
        upd = (
            update(HabitsOrm)
            .where(HabitsOrm.id == id)
            .values(**data)
            .returning(HabitsOrm)
        )
        new_habit = await self.session.execute(upd)
        updated_habit = new_habit.scalars().one_or_none()
        return updated_habit
