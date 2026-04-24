# custom


from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# project
from data import *

async_engine = create_async_engine(
    url=f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    echo=True,
)

session_factory = async_sessionmaker(bind=async_engine, autoflush=True, expire_on_commit=False)

class Base(declarative_base):
    pass
