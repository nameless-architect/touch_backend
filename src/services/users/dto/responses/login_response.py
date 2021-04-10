from typing import Optional

from pydantic import BaseModel


class LoginResponse(BaseModel):
    authenticated: bool
    jwt_token: Optional[str] = None
