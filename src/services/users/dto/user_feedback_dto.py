from typing import List

from pydantic.main import BaseModel

from services.users.db.models.base import UserFeedback
from services.users.dto.feedback_rating_dto import FeedbackRatingDTO


class UserFeedbackDTO(BaseModel):
    feedback_id: int
    feedback_from_user_name: str
    feedback_from_user_pic: str
    description: str
    ratings: List[FeedbackRatingDTO]

    @classmethod
    def create_from_user_feedback_db_model(cls, user_feedback: UserFeedback):
        ratings = [FeedbackRatingDTO(feedback_rating_type=rating.feedback_rating_type,
                                     feedback_rating_score=rating.feedback_rating_score)
                   for rating in user_feedback.feedback_ratings]

        return UserFeedbackDTO(feedback_id=user_feedback.id,
                               feedback_from_user_name=user_feedback.feedback_from_user.first_name,
                               feedback_from_user_pic='url',
                               description=user_feedback.description,
                               ratings=ratings)
