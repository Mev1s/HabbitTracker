from pydantic import BaseModel, Field, ConfigDict
from typing import Annotated
from datetime import datetime


class UserBase(BaseModel):
    telegram_id: Annotated[int, Field(description="Telegram unique user id", gt=0)]


class UserCreate(UserBase):
    pass


class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    account_created_at: Annotated[datetime, Field(description="Account created time")]
