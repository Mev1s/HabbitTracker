from fastapi import HTTPException
from ..repository.habitRepo import HabitRepository


class habitService:
    def __init__(self, session):
        self.session = session

    async def get_all_habits(self):
        result = await HabitRepository(self.session).get_all_habits()
        if not result:
            raise HTTPException(status_code=404, detail="Habit not found")
        return result
