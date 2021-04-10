from services.users.bl.feedback.managers.feedback_manger import FeedbackManager
from services.users.bl.managers.user_manager import UserManager
from services.users.dal.feedback_dal import FeedbackDAL
from services.users.dal.user_dal import UserDAL
from services.users.db.users_db_session import UsersDBSession
from services.users.dto.user_feedback_dto import UserFeedbackDTO


class GetUserFeedbacksQH:

    def __init__(self, user_mgr: UserManager,
                 feedback_mgr: FeedbackManager):
        self._user_mgr = user_mgr
        self._feedback_mgr = feedback_mgr

    def do_query(self, uid: str):
        with UsersDBSession():
            user_id = self._user_mgr.resolve_user_id_from_uid(uid)
            user_feedbacks = self._feedback_mgr.get_user_feedbacks(user_id)
            response = [UserFeedbackDTO.create_from_user_feedback_db_model(user_feedback) for user_feedback in
                        user_feedbacks]
            return response

    @classmethod
    def construct(cls):
        user_dal = UserDAL()
        feedback_dal = FeedbackDAL()
        user_mgr = UserManager(user_dal)
        feedback_mgr = FeedbackManager(feedback_dal)
        return cls(user_mgr, feedback_mgr)
