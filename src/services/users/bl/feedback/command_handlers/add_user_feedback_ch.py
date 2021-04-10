from typing import List

from services.users.bl.feedback.managers.feedback_manger import FeedbackManager
from services.users.bl.managers.user_manager import UserManager
from services.users.dal.feedback_dal import FeedbackDAL
from services.users.dal.user_dal import UserDAL
from services.users.db.users_db_session import UsersDBSession
from services.users.dto.feedback_rating_dto import FeedbackRatingDTO


class AddUserFeedbackCH:

    def __init__(self, user_mgr: UserManager,
                 feedback_mgr: FeedbackManager):
        self._user_mgr = user_mgr
        self._feedback_mgr = feedback_mgr

    def do_logic(self, feedback_from_uid: str, feedback_about_uid: str,
                 description: str, ratings: List[FeedbackRatingDTO]):
        with UsersDBSession():
            from_user_id = self._user_mgr.resolve_user_id_from_uid(feedback_from_uid)
            about_user_id = self._user_mgr.resolve_user_id_from_uid(feedback_about_uid)
            return self._feedback_mgr.add_feedback_to_user(from_user_id,
                                                           about_user_id,
                                                           description,
                                                           ratings)

    @classmethod
    def construct(cls):
        user_dal = UserDAL()
        feedback_dal = FeedbackDAL()
        user_mgr = UserManager(user_dal)
        feedback_mgr = FeedbackManager(feedback_dal)
        return cls(user_mgr, feedback_mgr)
