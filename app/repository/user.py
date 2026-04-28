from app.database.models import UsersOrm
from sqlalchemy import  select, update

class UserRepository:
    def __init__(self, session):
        self.session = session