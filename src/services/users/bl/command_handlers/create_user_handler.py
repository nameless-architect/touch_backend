from common.hashing.hashing_helper import HashingHelper
from services.users.bl.managers.user_details_manager import UserDetailsManager
from services.users.dal.user_dal import UserDAL
from services.users.db.users_db_session import UsersDBSession


class CreateUserHandler:

    def __init__(self,
                 user_details_manager: UserDetailsManager,
                 hashing_helper: HashingHelper):
        self._user_details_manager = user_details_manager
        self._hashing_helper = hashing_helper

    def create_user(self, email: str, password: str, user_account_type: str):
        with UsersDBSession():
            hashed_password = self._hashing_helper.hash_password(password)
            return self._user_details_manager.create_user(email, hashed_password, user_account_type)

    @classmethod
    def construct(cls):
        user_dal = UserDAL()
        user_details_manager = UserDetailsManager(user_dal)
        hashing_helper = HashingHelper()
        return cls(user_details_manager,
                   hashing_helper)
