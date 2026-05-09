from datetime import datetime

from sqlalchemy import select

from ..database.models import UsersOrm, HabitsOrm, HabitsLogsOrm


class HabitLogRepository:
    def __init__(self, session):
        self.session = session

    async def get_all_habit_logs(self):
        result = await self.session.execute(select(HabitsLogsOrm))
        return result.scalars().all()

    async def get_habit_log_by_id(self, habit_log_id: int):
        result = await self.session.execute(select(HabitsLogsOrm).where(HabitsLogsOrm.id == habit_log_id))
        return result.scalars().all()

    async def get_habit_logs_by_habit_id(self, habits_id: list[int]):
        result = await self.session.execute(
            select(HabitsLogsOrm).where(HabitsLogsOrm.habit_id.in_(habits_id))
        )
        return result.scalars().all()

    async def get_habit_logs_by_habit_date(self, start, end):
        result = await self.session.execute(select(HabitsLogsOrm).where(HabitsLogsOrm.complete_at.between(start, end)))
        return result.scalars().all()

    async def create_habit_log(self, data: HabitsLogsOrm):
        new_habit_log = HabitsLogsOrm(**data.model_dump())
        self.session.add(new_habit_log)
        return new_habit_log
