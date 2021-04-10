from services.users.bl.feedback.managers.feedback_manger import FeedbackManager
from services.users.dal.feedback_dal import FeedbackDAL
from services.users.db.users_db_session import UsersDBSession


class DeleteUserFeedbackCH:

    def __init__(self,
                 feedback_mgr: FeedbackManager):
        self._feedback_mgr = feedback_mgr

    def do_logic(self, feedback_id: int):
        with UsersDBSession():
            return self._feedback_mgr.delete_feedback(feedback_id)

    @classmethod
    def construct(cls):
        feedback_dal = FeedbackDAL()
        feedback_mgr = FeedbackManager(feedback_dal)
        return cls(feedback_mgr)
