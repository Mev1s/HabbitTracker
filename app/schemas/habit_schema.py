from typing import Annotated, Optional
from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class HabitBase(BaseModel):
    title: Annotated[str, Field(description="Title of the habit")]
    description: Annotated[
        Optional[str],
        Field(
            description="Description of the habit", default="No description provided"
        ),
    ]
    user_id: Annotated[int, Field(description="User id of the habit to UsersOrm")]


class HabitCreate(HabitBase):
    pass


class HabitResponse(HabitBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
