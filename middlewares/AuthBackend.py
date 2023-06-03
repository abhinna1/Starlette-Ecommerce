from starlette.authentication import AuthenticationBackend, AuthCredentials, SimpleUser, UnauthenticatedUser
import base64
import binascii
from services.session_services import SessionServices
from services.user_services import UserServices

class AuthBackend(AuthenticationBackend):

    async def authenticate(self, request):
        session_service = SessionServices(request.app.state.db)

        if "Authorization" not in request.headers:
            return None
        session = request.headers['Authorization']
        session = session.split(" ")[1]
        session = session_service.get_session_by_id(session)
        if session:
            if not session.is_active():
                return None
            return AuthCredentials(["authenticated"]), session.user
        return None