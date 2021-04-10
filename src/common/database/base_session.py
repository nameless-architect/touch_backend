from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, Session


class BaseSession:

    OPEN_SESSION = {}

    def __init__(self, db_name: str):
        self._session: Session = None
        self._engine = create_engine('postgresql+psycopg2://postgres:superman@localhost/{}'.format(db_name), echo=True)

    def __enter__(self):
        session_cls = sessionmaker(bind=self._engine)
        self._session = session_cls()
        BaseSession.OPEN_SESSION[self.__class__.__name__] = self._session
        return self._session

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not exc_type:
            self._session.commit()
        else:
            self._session.rollback()

        self._session = None

    @classmethod
    def get_session(cls):
        if not BaseSession.OPEN_SESSION.get(cls.__name__):
            raise Exception('There is no open session')
        return BaseSession.OPEN_SESSION.get(cls.__name__)

    @classmethod
    def with_session(cls):
        with cls() as db_session:
            return db_session
