from starlette.routing import Route
from controllers.user_controller import (
    login,
    getUser,
    register,
)
from routes.BaseRoute import BaseRoute

class UserRoutes(BaseRoute):
    routes = [
        Route('/', endpoint=getUser, methods=['GET']),
        Route('/register', endpoint=register, methods=['POST']),
        Route('/login', endpoint=login, methods=['POST']),
        
    ]