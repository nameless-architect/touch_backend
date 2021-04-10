from common.database.base_session import BaseSession


class UsersDBSession(BaseSession):
    DB_NAME = 'users_db'

    def __init__(self):
        super().__init__(self.DB_NAME)
