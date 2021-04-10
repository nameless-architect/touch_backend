from services.communication.db.communication_db_session import CommunicationDBSession
from services.communication.db.models.message import Message


class MessagesDAL:

    def __init__(self):
        pass

    @property
    def db_session(self):
        return CommunicationDBSession.get_session()

    def create_personal_messages(self, from_uid: str, to_uid: str, content: str, content_type: str) -> Message:
        message = Message(from_uuid=from_uid, to_uuid=to_uid, content=content, content_type=content_type)
        self.db_session.add(message)
        self.db_session.flush()
        return message

    def get_messages_sent_to_user(self, to_uid: str):
        pass

    def get_messages_sent_from_user(self, from_uid: str):
        pass
