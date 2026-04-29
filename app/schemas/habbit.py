from pydantic import BaseModel, Field, ConfigDict
from typing import Annotated
from datetime import datetime


class HabitBase(BaseModel):
    title: Annotated[str, Field(description="Title of the habit")]
    description: Annotated[str, Field(description="Description of the habit")]
    user_id: Annotated[int, Field(description="User id of the habit to UsersOrm")]


class HabitCreate(HabitBase):
    pass


class HabitResponse(HabitBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: Annotated[datetime, Field(description="Created at of the habit")]
