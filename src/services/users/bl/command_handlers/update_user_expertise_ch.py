from services.users.bl.managers.user_expertise_manager import UserExpertiseManager
from services.users.dal.expertises_dal import ExpertisesDAL
from services.users.db.users_db_session import UsersDBSession
from services.users.dto.user_expertises_dto import UserExpertiseDTO


class UpdateUserExpertiseCH:

    def __init__(self,
                 user_expertise_mgr: UserExpertiseManager):
        self._user_expertise_mgr = user_expertise_mgr

    def do_logic(self, uid: str, expertise_id: int, expertise_name: str):
        with UsersDBSession():
            expertise = self._user_expertise_mgr.get_expertise(expertise_id)
            self._validate_action(expertise, uid)
            expertise.expertise_name = expertise_name

            return UserExpertiseDTO(id=expertise.id, expertise_name=expertise.expertise_name)

    @staticmethod
    def _validate_action(expertise, uid):
        if expertise.uid != uid:
            raise Exception('Expertise not belongs to the customer')
        if expertise.deleted:
            raise Exception('Can update deleted expertise')

    @classmethod
    def construct(cls):
        expertises_dal = ExpertisesDAL()
        user_expertise_mgr = UserExpertiseManager(expertises_dal)
        return cls(user_expertise_mgr)
