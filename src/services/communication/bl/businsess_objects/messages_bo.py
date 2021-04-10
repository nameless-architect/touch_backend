from services.communication.dal.messages_dal import MessagesDAL


class MessagesBO:

    def __init__(self, message_dal: MessagesDAL):
        self._messages_dal = message_dal

    def create_personal_message(self, from_uid: str, to_uid: str, content: str, content_type: str):
        return self._messages_dal.create_personal_messages(from_uid, to_uid, content, content_type)

    def get_messages_sent_to_user(self, to_uid: str):
        pass

    def get_messages_sent_from_user(self, from_uid: str):
        pass
