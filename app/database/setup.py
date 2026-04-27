from .base import Base
from .config import async_engine
from .models import UsersOrm, HabitsOrm


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
