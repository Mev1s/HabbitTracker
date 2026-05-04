from pydantic import BaseModel, Field, ConfigDict

from typing import Annotated
from datetime import datetime


class HabitLogsBase(BaseModel):
    habit_id: Annotated[int, Field(description="Habit foreign key ID to habits")]

class HabitLogsCreate(HabitLogsBase):
    pass

class HabitLogsResponse(HabitLogsBase):
    model_config = ConfigDict(from_attributes=True)

    id: Annotated[int, Field(description="Habit log ID")]
    complete_at: Annotated[datetime, Field(description="Habit log complete at time")]