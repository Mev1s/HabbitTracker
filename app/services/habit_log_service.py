from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..repository.habit_log_repository import HabitLogRepository

class HabitLogsService:
    def __init__(self, session):
        self.session = session

    async def get_all_habits_logs(self):
        result = await HabitLogRepository(self.session).get_all_habits_logs()
        if not result:
            raise HTTPException(status_code=404, detail="No habits logs")
        return result