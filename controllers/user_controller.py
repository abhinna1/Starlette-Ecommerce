from starlette.requests import Request
from starlette.responses import JSONResponse
from services.user_services import UserServices

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
