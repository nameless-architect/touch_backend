from services.users.dal.user_account_dal import UserAccountDAL


class UserAccountManager:

    def __init__(self, user_account_dal: UserAccountDAL):
        self._user_account_dal = user_account_dal

    def get_user_by_email_and_password(self, email: str):
        return self._user_account_dal.get_user_account_by_email_and_password(email)
