from fastapi import HTTPException

from ..repository.habit_log_repository import HabitLogRepository
from ..repository.user_repository import UserRepository
from ..repository.habit_repository import HabitRepository


class HabitLogsService:
    def __init__(self, session):
        self.session = session

    async def get_all_habit_logs(self):
        result = await HabitLogRepository(self.session).get_all_habits_logs()
        if not result:
            raise HTTPException(status_code=404, detail="No habits logs")
        return result

    async def get_habit_logs_by_id(self, habit_log_id: int):
        result = await HabitLogRepository(self.session).get_habit_logs_by_id(habit_log_id)
        if not result:
            raise HTTPException(status_code=404, detail="No habit logs")
        return result

    async def get_habit_logs_by_telegram_id(self, telegram_id: int):
        habits_id = []

        user = await UserRepository(self.session).get_user_by_telegram_id(int(telegram_id))
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        user_habits = await HabitRepository(self.session).get_habits_by_user_id(user.id)
        if not user_habits:
            raise HTTPException(status_code=404, detail="Habits not found")

        for habit in user_habits:
            habits_id.append(habit.id)

        habit_logs = await HabitLogRepository(self.session).get_habit_logs_by_habit_id(habits_id)
        if not habit_logs:
            raise HTTPException(status_code=404, detail="Habit logs not found")

        return habit_logs


