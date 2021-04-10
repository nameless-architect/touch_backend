from pydantic import BaseModel


class UserExpertiseDTO(BaseModel):
    id: int
    expertise_name: str
