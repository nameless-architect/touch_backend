from fastapi import APIRouter

router = APIRouter()


@router.post("messages/send_text_message")
def sent_personal_text_message(from_uid: str, to_uid: str, content: str):
    pass


@router.post("messages/send_file")
def sent_a_personal_file(from_uid: str, to_uid, file_content: str):
    pass


@router.get("messages/get_messages_to_user/{to_uid}")
def get_messages_to_user(to_uid: str):
    pass


@router.get("messages/get_messages_from_user/{from_uid}")
def get_messages_from_user(from_uid: str):
    pass
