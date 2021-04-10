from sqlalchemy import Column, DateTime, String, Integer, func, Boolean

from services.communication.db.models import Base


class PayableMeetingLink(Base):
    __tablename__ = 'payable_meeting_links'

    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_uuid = Column(String(50))
    quest_uuid = Column(String(50), nullable=True)
    hidden_link = Column(String(1225))
    price_units = Column(Integer)
    paid = Column(Boolean)
