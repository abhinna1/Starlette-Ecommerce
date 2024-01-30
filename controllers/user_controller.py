from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.authentication import requires
from services.user_services import UserServices
from services.session_services import SessionServices
from asyncio import get_event_loop
from helpers.log_helpers import (
    log_success_user_registration,
    log_failed_user_registration,
)
from commons.ENUMS import UserEnum
from starlette import status

async def register(request: Request):
    data = await request.json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    cfm_password = data.get('cfm_password')
    event_loop = get_event_loop()
    try:
        user_service = UserServices(request.app.state.db)
        user_service.create_user(username, email, password, cfm_password)
        # await log_success_user_registration(email)
        event_loop.create_task(log_success_user_registration(email))
    except Exception as e:
        # await log_failed_user_registration(email, str(e))
        event_loop.create_task(log_failed_user_registration(email, str(e)))
        return JSONResponse({'message': str(e)}, status_code=400)
    
    # Example response
    response_data = {
        'messag e': 'User created successfully',
        'username': username,
        'email': email
    }
    return JSONResponse(response_data, status_code=status.HTTP_201_CREATED)

async def login(request: Request, email=None, password=None):
    if not email and not password:
        data = await request.json()
        email = data.get('email')
        password = data.get('password')
    try:
        session_service = SessionServices(request.app.state.db)
        session = session_service.create_session(email, password)
        response_data={
            "id": str(session.id),
            "user": str(session.user_id),
            "created_at": str(session.created_at),
            "expires_at": str(session.expires_at),
            "is_expired": session.is_expired
        }
        return JSONResponse(response_data)
    except Exception as e:
        
        return JSONResponse({'message': str(e)}, status_code=400)
    
@requires('authenticated')
async def getUser(request:Request):
    user = request.user
    response_data = {
        "id": str(user.id),
        "email": user.email,
        "username": user.username
    }
    return JSONResponse(response_data)

@requires('authenticated')
async def logout(request: Request):
    user = request.user
    data = await request.json()
    try:
        session_service = SessionServices(request.app.state.db)
        session = session_service.get_session_by_id(data['session_id'])
        session.is_expired = True
        request.app.state.db.commit()
        return JSONResponse({'message': 'Logout successful'}, status_code=200)
    except Exception as e:
        return JSONResponse({'message': str(e)}, status_code=400)
    
@requires(scopes=['authenticated', 'admin'])
async def isAdmin(request: Request):
    if request.user.role == UserEnum.ADMIN:
        return JSONResponse({'message': 'Admin only page.'}, status_code=status.HTTP_200_OK)
    return JSONResponse({'message': 'Unauthorized.'}, status_code=status.HTTP_401_UNAUTHORIZED)
