from sqlalchemy import select

from ..database.models import UsersOrm, HabitsOrm, HabitsLogsOrm


class HabitLogRepository:
    def __init__(self, session):
        self.session = session

    async def get_all_habit_logs(self):
        result = await self.session.execute(select(HabitsLogsOrm))
        return result.scalars().all()

    async def get_habit_logs_by_id(self, habit_log_id: int):
        result = await self.session.execute(select(HabitsLogsOrm))
        return result.scalars().all()

    async def get_habit_logs_by_habit_id(self, habits_id: list[int]):
        result = await self.session.execute(
            select(HabitsLogsOrm).where(HabitsLogsOrm.habit_id.in_(habits_id))
        )
        return result.scalars().one_or_none()
