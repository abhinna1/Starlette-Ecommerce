from starlette.authentication import AuthenticationBackend, AuthCredentials, SimpleUser, UnauthenticatedUser
import base64
import binascii
from services.session_services import SessionServices
from services.user_services import UserServices
from commons.ENUMS import UserEnum
class AuthBackend(AuthenticationBackend):

    async def authenticate(self, request):
        try:
            session_service = SessionServices(request.app.state.db)
            if "Authorization" not in request.headers:
                return None
            session = request.headers['Authorization']
            session = session.split(" ")[1]
            session = session_service.get_session_by_id(session)
            if session:
                if not session.is_active():
                    return None
                if session.user.failed_login > 5:
                    return None
                if session.user.role == UserEnum.ADMIN:
                    session.user.failed_login = 0
                    return AuthCredentials(["authenticated", "admin"]), session.user
                session.user.failed_login = 0
                return AuthCredentials(["authenticated"]), session.user
            return None
        except Exception as e:
            request.app.state.db.rollback()
            return None