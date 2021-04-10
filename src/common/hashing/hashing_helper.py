from passlib.context import CryptContext


class HashingHelper:

    def __init__(self):
        self._crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def hash_password(self, password: str):
        return self._crypt_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password : str):
        return self._crypt_context.verify(plain_password, hashed_password)
