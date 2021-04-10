from services.communication.bl.businsess_objects.messages_bo import MessagesBO
from services.communication.dal.messages_dal import MessagesDAL
from services.communication.db.communication_db_session import CommunicationDBSession


class SendAPersonalTextMessagesBP:

    def __init__(self, messages_bo: MessagesBO):
        self._messages_bo: MessagesBO = messages_bo

    def do_logic(self, from_uid: str, to_uid: str, content: str):
        content_type = 'text'
        with CommunicationDBSession():
            self._messages_bo.create_personal_message(from_uid, to_uid, content, content_type)

    @classmethod
    def construct(cls):
        messages_dal = MessagesDAL()
        messages_bo = MessagesBO(messages_dal)
        return cls(messages_bo)
