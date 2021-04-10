from services.users.dal.base_users_service_dal import BaseUsersServiceDAL
from services.users.db.models.base import UserAccount


class UserAccountDAL(BaseUsersServiceDAL):

    def get_user_account_by_email_and_password(self, email: str) -> UserAccount:
        user_account = self.db_session.query(UserAccount).filter(UserAccount.email == email).\
            one_or_none()
        return user_account
