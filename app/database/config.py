from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from data import *

async_engine = create_async_engine(
    url=f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    echo=True,
)
async_session_factory = async_sessionmaker(
    bind=async_engine, expire_on_commit=False, class_=AsyncSession
)
