from services.users.bl.managers.user_expertise_manager import UserExpertiseManager
from services.users.dal.expertises_dal import ExpertisesDAL
from services.users.db.users_db_session import UsersDBSession
from services.users.dto.user_expertises_dto import UserExpertiseDTO


class GetUserExpertisesQH:

    def __init__(self, user_expertises_mgr: UserExpertiseManager):
        self._user_expertises_mgr = user_expertises_mgr

    def do_query(self, uid: str):
        with UsersDBSession():
            user_expertises = self._user_expertises_mgr.get_user_expertises(uid)
            response = [UserExpertiseDTO(id=db_model.id, expertise_name=db_model.expertise_name) for db_model in
                        user_expertises]
            return response

    @classmethod
    def construct(cls):
        expertises_dal = ExpertisesDAL()
        user_expertise_mgr = UserExpertiseManager(expertises_dal)
        return cls(user_expertise_mgr)
