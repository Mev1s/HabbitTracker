from sqlalchemy import (
    Table,
    Column,
    MetaData,
    BigInteger,
    ForeignKey,
)
from datetime import date
from sqlalchemy.orm import mapped_column, Mapped
from typing import Annotated


from .base import Base

class UsersOrm(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int] = mapped_column(BigInteger)
    telegram_id: Mapped[int] = mapped_column(BigInteger)


class HabitsOrm(Base):
    __tablename__ = "habits"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    description: Mapped[str | None]
    created_at: Mapped[date] = mapped_column(default=date.today)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
