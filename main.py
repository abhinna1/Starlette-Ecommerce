from starlette.applications import Starlette
from starlette.routing import Route, Mount
from controllers.user_controller import register, login, getUser
from database import SessionLocal
from middlewares.AuthBackend import AuthBackend
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.middleware import Middleware
from routes.product_routes import ProductRoutes
from controllers.cart_controller import add_product_to_cart, get_user_cart
from cryptography.fernet import Fernet
import os
from routes.UserRoutes import UserRoutes 
from starlette.middleware.cors import CORSMiddleware
# from admin.admin import admin as app_admin
# Init application.
routes = [
    Mount("/user", routes=UserRoutes.routes),
    Mount("/product", routes=ProductRoutes.routes),
    Route("/cart", endpoint=add_product_to_cart, methods=["POST"]),
    Route("/cart", endpoint=get_user_cart, methods=["GET"])
    
]

# Define middleware

# Middlewares.
auth_backend = AuthBackend()
middlewares = [
    Middleware(AuthenticationMiddleware, backend=AuthBackend()),
    Middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])
]

key = bytes(os.getenv("FERNET_PRIVATE_KEY").encode('utf-8'))
cryptographer = Fernet(key=key)

app = Starlette(
    routes=routes,
    middleware=middlewares,
)

# app_admin.mount_to(app)


# Application states.
app.state.db = SessionLocal()
app.state.cryptographer = cryptographer

# enc = app.state.cryptographer.encrypt('1')
# print('enc', enc)
# dec = app.state.cryptographer.decrypt(enc)
# print('dec', dec)

# Run application.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )