from services.communication.bl.businsess_objects.messages_bo import MessagesBO
from services.communication.dal.messages_dal import MessagesDAL


class SendAPersonalTextMessagesBP:

    def __init__(self, messages_bo: MessagesBO):
        self._messages_bo = MessagesBO

    def do_logic(self, from_uid: str, to_uid: str, content: str):
        pass

    @classmethod
    def construct(cls):
        messages_dal = MessagesDAL()
        messages_bo = MessagesBO(messages_dal)
        return cls(messages_bo)
