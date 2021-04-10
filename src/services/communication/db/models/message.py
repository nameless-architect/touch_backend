from sqlalchemy import Column, DateTime, String, Integer, func

from services.users.db.models.base import Base


class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True, autoincrement=True)
    from_uuid = Column(String(50))
    to_uuid = Column(String(50))
    content = Column(String(2255))
    content_type = Column(String)
