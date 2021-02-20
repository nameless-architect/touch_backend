from pydantic import BaseModel


class SendAPersonalTextMessageCmd(BaseModel):
    from_uid: str
    to_uid: str
    content: str
