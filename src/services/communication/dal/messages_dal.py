
class MessagesDAL:

    def __init__(self):
        pass

    def create_personal_messages(self, from_uid: str, to_uid: str, content: str, content_type: str):
        pass

    def get_messages_sent_to_user(self, to_uid: str):
        pass

    def get_messages_sent_from_user(self, from_uid: str):
        pass
