from starlette.requests import Request
from abstracts.CartAbstract import CartItemAbstract, DbCartItemAbstract
from services.cart_services import CartServices
from starlette.authentication import requires
from starlette.responses import JSONResponse
from starlette import status
from cryptography.fernet import Fernet
