from services.users.dal.user_dal import UserDAL


class UserDetailsManager:

    def __init__(self, user_dal: UserDAL):
        self._user_dal = user_dal

    def create_user(self, email: str, password: str, user_account_type: str):
        user = self._user_dal.create_user(email, password, user_account_type)
        return user.uid
