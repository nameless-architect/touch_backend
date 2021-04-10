from services.users.bl.managers.user_expertise_manager import UserExpertiseManager
from services.users.bl.managers.user_manager import UserManager
from services.users.dal.expertises_dal import ExpertisesDAL
from services.users.dal.user_dal import UserDAL
from services.users.db.users_db_session import UsersDBSession


class AddUserExpertiseCH:

    def __init__(self, user_mgr: UserManager,
                 user_expertise_mgr: UserExpertiseManager):
        self._user_mgr = user_mgr
        self._user_expertise_mgr = user_expertise_mgr

    def do_logic(self, uid: str, expertise_name: str):
        with UsersDBSession():
            user_id = self._user_mgr.resolve_user_id_from_uid(uid)
            expertise_id = self._user_expertise_mgr.add_user_expertise(user_id, uid, expertise_name)
            return expertise_id

    @classmethod
    def construct(cls):
        users_dal = UserDAL()
        expertises_dal = ExpertisesDAL()

        users_mgr = UserManager(users_dal)
        user_expertise_mgr = UserExpertiseManager(expertises_dal)

        return cls(users_mgr, user_expertise_mgr)
