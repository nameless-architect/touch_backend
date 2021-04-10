from typing import Any

from sqlalchemy.orm import Session

from services.users.db.users_db_session import UsersDBSession


class BaseUsersServiceDAL:

    def __init__(self):
        pass

    @property
    def db_session(self) -> Session:
        return UsersDBSession.get_session()

    def add_and_flush(self, model: Any):
        self.db_session.add(model)
        self.db_session.flush()
