from datetime import datetime, timedelta

from jose import jwt

from common.json_web_token.jwt_config import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM


class JWTHelper:

    def encode_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    def decode_access_token(self, token: str):
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

