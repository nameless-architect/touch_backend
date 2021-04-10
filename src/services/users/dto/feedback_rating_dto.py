from pydantic import BaseModel


class FeedbackRatingDTO(BaseModel):
    feedback_rating_type: str
    feedback_rating_score: int
