from typing import List

from services.users.dal.base_users_service_dal import BaseUsersServiceDAL
from services.users.db.models.base import UserExpertise


class ExpertisesDAL(BaseUsersServiceDAL):

    def get_user_expertise_by_id(self, expertise_id: int) -> UserExpertise:
        return self.db_session.query(UserExpertise).get(expertise_id)

    def get_user_expertises(self, uid: str, only_active: bool = True) -> List[UserExpertise]:
        query = self.db_session.query(UserExpertise). \
            filter(UserExpertise.uid == uid)

        if only_active:
            query = query.filter(UserExpertise.deleted != True)

        return query.all()

    def add_expertise_to_user(self, user_id: int, uid: str, expertise_name: str,
                              expertise_level: int = 0) -> UserExpertise:
        user_expertise = UserExpertise(user_id=user_id, uid=uid, expertise_name=expertise_name,
                                       expertise_leve=expertise_level)
        self.add_and_flush(user_expertise)
        return user_expertise
