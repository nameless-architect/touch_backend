from services.users.dal.user_dal import UserDAL


class UserManager:

    def __init__(self, user_dal: UserDAL):
        self._user_dal = user_dal

    def resolve_user_id_from_uid(self, uid: str) -> int:
        user = self._user_dal.get_user_by_uid(uid)
        return user.id

