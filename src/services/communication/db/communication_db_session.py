from common.database.base_session import BaseSession


class CommunicationDBSession(BaseSession):
    DB_NAME = "messaging_db"

    def __init__(self):
        super().__init__(self.DB_NAME)
