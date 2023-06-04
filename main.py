from starlette.applications import Starlette
from starlette.routing import Route, Mount
from controllers.user_controller import register, login, getUser
from database import SessionLocal
from middlewares.AuthBackend import AuthBackend
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware import Middleware
# from admin.admin import admin as app_admin
# Init application.
routes = [
    Route("/register", endpoint=register, methods=["POST"]),
    Route("/login", endpoint=login, methods=["POST"]),
    Route("/user", endpoint=getUser, methods=["GET"]),
]

# Middlewares.
auth_backend = AuthBackend()
middlewares = [
    Middleware(AuthenticationMiddleware, backend=AuthBackend())
]

app = Starlette(
    routes=routes,
    middleware=middlewares
)

# app_admin.mount_to(app)


# Application states.
app.state.db = SessionLocal()

# Run application.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
