from services.users.dal.expertises_dal import ExpertisesDAL
from services.users.db.models.base import UserExpertise


class UserExpertiseManager:

    def __init__(self, expertise_dal: ExpertisesDAL):
        self._expertise_dal = expertise_dal

    def get_expertise(self, expertise_id: int) -> UserExpertise:
        return self._expertise_dal.get_user_expertise_by_id(expertise_id)

    def get_user_expertises(self, uid: str):
        return self._expertise_dal.get_user_expertises(uid)

    def add_user_expertise(self, user_id: int, uid: str, expertise_name: str):
        return self._expertise_dal.add_expertise_to_user(user_id, uid, expertise_name)
