from common.hashing.hashing_helper import HashingHelper
from common.json_web_token.jwt_helper import JWTHelper
from services.users.bl.managers.user_account_manager import UserAccountManager
from services.users.bl.managers.user_expertise_manager import UserExpertiseManager
from services.users.dal.expertises_dal import ExpertisesDAL
from services.users.dal.user_account_dal import UserAccountDAL
from services.users.db.users_db_session import UsersDBSession
from services.users.dto.queries.login_query import LoginQuery
from services.users.dto.responses.login_response import LoginResponse
from services.users.dto.user_expertises_dto import UserExpertiseDTO


class LoginQH:

    def __init__(self, user_account_mgr: UserAccountManager,
                 jwt_helper: JWTHelper,
                 hashing_helper: HashingHelper):
        self._user_account_mgr = user_account_mgr
        self._jwt_helper = jwt_helper
        self._hashing_helper = hashing_helper

    def do_query(self, logic_q: LoginQuery):
        with UsersDBSession():
            user_account = self._user_account_mgr.get_user_by_email_and_password(logic_q.email)
            if user_account and self._hashing_helper.verify_password(logic_q.password, user_account.password):
                data = {'sub': user_account.uid}
                return LoginResponse(authenticated=True,
                                     jwt_token=self._jwt_helper.encode_access_token(data))
            else:
                return LoginResponse(authenticated=False)

    @classmethod
    def construct(cls):
        user_account_dal = UserAccountDAL()
        user_account_mgr = UserAccountManager(user_account_dal)
        jwt_helper = JWTHelper()
        hashing_helper = HashingHelper()
        return cls(user_account_mgr,
                   jwt_helper,
                   hashing_helper)
