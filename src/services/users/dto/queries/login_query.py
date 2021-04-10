from pydantic.main import BaseModel


class LoginQuery(BaseModel):
    email: str
    password: str
