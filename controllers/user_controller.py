from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.authentication import requires
from services.user_services import UserServices
from services.session_services import SessionServices


async def register(request: Request):
    data = await request.json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    cfm_password = data.get('cfm_password')
    
    try:
        user_service = UserServices(request.app.state.db)
        user_service.create_user(username, email, password, cfm_password)
    except Exception as e:
        return JSONResponse({'message': str(e)}, status_code=400)
    
    # Example response
    response_data = {
        'message': 'User created successfully',
        'username': username,
        'email': email
    }
    return JSONResponse(response_data)

async def login(request: Request):
    data = await request.json()
    email = data.get('email')
    password = data.get('password')
    try:
        session_service = SessionServices(request.app.state.db)
        session = session_service.create_session(email, password)
        response_data={
            "id": str(session.id),
            "user": session.user_id,
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
        "id": user.id,
        "email": user.email,
        "username": user.username
    }
    return JSONResponse(response_data)