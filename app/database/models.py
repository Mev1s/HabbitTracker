from datetime import datetime

from sqlalchemy import Table, Column, MetaData, BigInteger, ForeignKey, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped


from .base import Base


class UsersOrm(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    account_created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )


class HabitsOrm(Base):
    __tablename__ = "habits"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str | None] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))


class HabitsLogsOrm(Base):
    __tablename__ = "habit_logs"
    id: Mapped[int] = mapped_column(primary_key=True)
    complete_at: Mapped[datetime] = mapped_column(server_default=func.now())
    habit_id: Mapped[int] = mapped_column(ForeignKey("habits.id", ondelete="CASCADE"))
