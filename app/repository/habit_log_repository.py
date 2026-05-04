from sqlalchemy import select

from ..database.models import UsersOrm, HabitsOrm, HabitsLogsOrm


class HabitLogRepository:
    def __init__(self, session):
        self.session = session

    async def get_all_habits_logs(self):
        result = await self.session.execute(select(HabitsLogsOrm))
        return result.scalars().all()