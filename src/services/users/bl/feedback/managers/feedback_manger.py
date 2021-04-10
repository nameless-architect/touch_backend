from typing import Optional, List

from services.users.dal.feedback_dal import FeedbackDAL
from services.users.db.models.base import UserFeedback
from services.users.dto.feedback_rating_dto import FeedbackRatingDTO


class FeedbackManager:

    def __init__(self, feedback_dal: FeedbackDAL):
        self._feedback_dal = feedback_dal

    def add_feedback_to_user(self, feedback_from_user_id: int, feedback_about_user_id: int,
                             description: Optional[str],
                             ratings: List[FeedbackRatingDTO]):
        return self._feedback_dal.add_feedback_to_user(feedback_from_user_id, feedback_about_user_id,
                                                       description,
                                                       ratings)

    def get_user_feedbacks(self, user_id: int) -> List[UserFeedback]:
        return self._feedback_dal.get_user_feedbacks(user_id)

    def update_feedback(self, feedback_id: int,
                        description: Optional[str],
                        ratings: List[FeedbackRatingDTO]):
        feedback = self._feedback_dal.get_feedback_by_id(feedback_id)
        feedback.description = description
        for feedback_rating in feedback.feedback_ratings:
            for rating in ratings:
                if rating.feedback_rating_type == feedback_rating.feedback_rating_type:
                    feedback_rating.feedback_rating_score = rating.feedback_rating_score
                    break

    def delete_feedback(self, feedback_id: int):
        self._feedback_dal.delete_feedback(feedback_id)
