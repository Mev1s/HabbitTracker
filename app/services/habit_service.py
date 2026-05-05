from fastapi import HTTPException

from ..repository.habit_repository import HabitRepository
from ..repository.user_repository import UserRepository


class habitService:
    def __init__(self, session):
        self.session = session

    async def get_all_habits(self):
        result = await HabitRepository(self.session).get_all_habits()
        if not result:
            raise HTTPException(status_code=404, detail="Habit not found")
        return result

    async def get_habits_by_title(self, title: str):
        result = await HabitRepository(self.session).get_habits_by_title(title)
        if not result:
            raise HTTPException(status_code=404, detail="Habit not found")
        return result

    async def get_habits_by_user_id(self, user_id: int):
        result = await HabitRepository(self.session).get_habits_by_user_id(user_id)
        if not result:
            raise HTTPException(status_code=404, detail="Habit not found")
        return result

    async def get_habits_by_user_telegram_id(self, telegram_id: int):
        user = await UserRepository(self.session).get_user_by_telegram_id(telegram_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        habits = await HabitRepository(self.session).get_habits_by_user_id(user.id)
        if not habits:
            raise HTTPException(status_code=404, detail="Habit not found")
        return habits

    async def create_habit(self, data):
        user = await UserRepository(self.session).get_user_by_id(data.user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        old_user_habits = await HabitRepository(self.session).get_habits_by_user_id(user.id)
        for habit in old_user_habits:
            if habit.title == data.title:
                raise HTTPException(status_code=409, detail="Habit already exists")

        new_habit = await HabitRepository(self.session).create_habit(data)

        await self.session.commit()
        await self.session.refresh(new_habit)
        return new_habit
