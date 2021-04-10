from typing import Optional, List

from sqlalchemy import not_

from services.users.dal.base_users_service_dal import BaseUsersServiceDAL
from services.users.db.models.base import FeedbackRating, UserFeedback
from services.users.dto.feedback_rating_dto import FeedbackRatingDTO


class FeedbackDAL(BaseUsersServiceDAL):

    def get_feedback_by_id(self, feedback_id: int) -> UserFeedback:
        return self.db_session.query(UserFeedback).get(feedback_id)

    def add_feedback_to_user(self, feedback_from_user_id: int, feedback_about_user_id: int,
                             description: Optional[str],
                             ratings: List[FeedbackRatingDTO]):
        feedback_rating = [FeedbackRating(feedback_rating_type=rating.feedback_rating_type,
                                          feedback_rating_score=rating.feedback_rating_score)
                           for rating in ratings]
        user_feedback = UserFeedback(feedback_from_user_id=feedback_from_user_id,
                                     feedback_about_user_id=feedback_about_user_id,
                                     description=description,
                                     feedback_ratings=feedback_rating)
        self.add_and_flush(user_feedback)
        return user_feedback

    def get_user_feedbacks(self, user_id: str, only_active: bool = True) -> List[UserFeedback]:
        query = self.db_session.query(UserFeedback) \
            .filter(UserFeedback.feedback_about_user_id == user_id)

        if only_active:
            query = query.filter(not_(UserFeedback.deleted))

        return query.all()

    def delete_feedback(self, feedback_id):
        self.db_session.query(FeedbackRating).filter(FeedbackRating.user_feedback_id == feedback_id).delete()
        self.db_session.query(UserFeedback).filter(UserFeedback.id == feedback_id).delete()