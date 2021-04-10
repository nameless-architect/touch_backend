from typing import List

import uvicorn
from fastapi import FastAPI, Body, UploadFile, File
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware

from common.s3.s3_client import S3Client
from services.communication.bl.business_processes.send_a_personal_text_message_bp import SendAPersonalTextMessagesBP
from services.users.bl.command_handlers.add_user_expertise_ch import AddUserExpertiseCH
from services.users.bl.command_handlers.create_user_handler import CreateUserHandler
from services.users.bl.command_handlers.remove_user_experties_ch import RemoveUserExpertiseCH
from services.users.bl.command_handlers.update_user_expertise_ch import UpdateUserExpertiseCH
from services.users.bl.command_handlers.upload_profile_icon_ch import UploadProfileIconCH
from services.users.bl.feedback.command_handlers.add_user_feedback_ch import AddUserFeedbackCH
from services.users.bl.feedback.command_handlers.delete_user_feedback_ch import DeleteUserFeedbackCH
from services.users.bl.feedback.query_handlers.get_user_feedbacks_qh import GetUserFeedbacksQH
from services.users.bl.query_handlers.get_user_expetises_qh import GetUserExpertisesQH
from services.users.bl.query_handlers.login_qh import LoginQH
from services.users.dto.commands.register_user import RegisterUser
from services.users.dto.feedback_rating_dto import FeedbackRatingDTO
from services.users.dto.queries.login_query import LoginQuery

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/messages/send_text_message")
def send_text_message(from_uid: str = Body(...), to_uid: str = Body(...), content: str = Body(...)):
    send_a_personal_text_message_bp = SendAPersonalTextMessagesBP.construct()
    send_a_personal_text_message_bp.do_logic(from_uid, to_uid, content)


# region Users
@app.post("/users/register_user")
def register_user(register_user_cmd: RegisterUser):
    handler = CreateUserHandler.construct()
    return handler.create_user(register_user_cmd.email, register_user_cmd.password, register_user_cmd.userType)


@app.post("/users/login")
def login(logic_q: LoginQuery):
    handler = LoginQH.construct()
    return handler.do_query(logic_q)


@app.post('/users/add_user_expertise')
def add_user_expertise(uid: str = Body(...), expertise_name: str = Body(...)):
    cmd_handler = AddUserExpertiseCH.construct()
    return cmd_handler.do_logic(uid, expertise_name)


@app.post('/users/update_user_expertise')
def update_user_expertise(uid: str = Body(...), expertise_id: int = Body(...), expertise_name: str = Body(...)):
    command_handler = UpdateUserExpertiseCH.construct()
    return command_handler.do_logic(uid, expertise_id, expertise_name)


@app.post('/users/remove_user_expertise')
def remove_user_expertise(uid: str = Body(...), expertise_id: int = Body(...)):
    command_handler = RemoveUserExpertiseCH.construct()
    command_handler.do_logic(uid, expertise_id)


@app.get('/users/{uid}/expertises')
def get_user_expertise(uid: str):
    query_handler = GetUserExpertisesQH.construct()
    return query_handler.do_query(uid)


# endregion Users

# region Feedbacks

@app.get('/users/{uid}/feedbacks')
def get_user_feedbacks(uid: str):
    query_handler = GetUserFeedbacksQH.construct()
    return query_handler.do_query(uid)


@app.post('/users/add_feedback_to_user')
def add_feedback_to_user(feedback_from_user_uid: str = Body(...),
                         feedback_about_user_uid: str = Body(...),
                         description: str = Body(...),
                         ratings: List[FeedbackRatingDTO] = Body(...)):
    command_handler = AddUserFeedbackCH.construct()
    command_handler.do_logic(feedback_from_user_uid, feedback_about_user_uid, description,
                             ratings)


@app.post('/users/delete_feedback')
def delete_feedback(feedback_id: int):
    command_handler = DeleteUserFeedbackCH.construct()
    command_handler.do_logic(feedback_id)


@app.post('/users/upload_profile_icon')
def upload_profile_icon(file: UploadFile = File(...)):
    command_handler = UploadProfileIconCH.construct()
    command_handler.do_logic(file)


@app.get('/content/video')
def get_content_video():
    s3_content = S3Client()
    with open('filename1.mp4', 'wb') as data:
        s3_content.get_file_object(data)
        return StreamingResponse(data, media_type="video/mp4")


# endregion Feedback


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
