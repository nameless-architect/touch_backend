from services.users.dal.base_users_service_dal import BaseUsersServiceDAL
from services.users.db.models.base import User, UserAccount


class UserDAL(BaseUsersServiceDAL):

    def get_user_by_uid(self, uid: str) -> User:
        return self.db_session.query(User).filter(User.uid == uid).one()

    def create_user(self, email: str, password: str, user_account_type: str) -> User:
        user = UserAccount(email=email, password=password, user_account_type=user_account_type)
        self.db_session.add(user)
        self.db_session.flush()
        return user
