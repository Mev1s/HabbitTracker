from fastapi import HTTPException

from app.repository.userRepo import UserRepository


class UserService:
    def __init__(self, session):
        self.session = session

    async def get_all_users(self):
        return await UserRepository(self.session).get_all_users()

    async def get_user_by_id(self, user_id: int):
        result = await UserRepository(self.session).get_user_by_id(user_id)
        if not result:
            raise HTTPException(status_code=404, detail="User not found")
        return result
