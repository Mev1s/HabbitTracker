from app.repository.userRepo import UserRepository


class UserService:
    def __init__(self, session):
        self.session = session

    async def get_all_users(self):
        return await UserRepository(self.session).get_all_users()
