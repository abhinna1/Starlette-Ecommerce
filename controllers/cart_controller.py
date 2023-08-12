from starlette.requests import Request
from abstracts.CartAbstract import CartItemAbstract, DbCartItemAbstract
from services.cart_services import CartServices
from starlette.authentication import requires
from starlette.responses import JSONResponse
from starlette import status
from cryptography.fernet import Fernet
from services.product_services import ProductServices
from helpers.log_helpers import (
    log_add_to_cart,
    create_audit_log,
)

@requires('authenticated')
async def add_product_to_cart(request:Request):
    try:
        data = await request.json()
        services = CartServices(db=request.app.state.db)
        product_services = ProductServices(db=request.app.state.db)
        cart = services.get_or_create_cart(user_id=request.user.id)

        product_id = data.get('product')
        quantity = data.get('quantity', 1)
        product = product_services.get_product_by_id(product_id)
        
        if quantity == 0:
            return JSONResponse({"message": "Quantity must be greater than 0."}, status_code=status.HTTP_400_BAD_REQUEST)
        
        cart_item = services.add_product_to_cart(
            cart_id = cart.id,
            product_id = product_id,
            quantity = quantity,
            user_id=request.user.id,
            cryptographer=request.app.state.cryptographer
        )
        
        if not cart_item:
            return JSONResponse({"message": "Product removed from cart."})
        
        # import pdb; pdb.set_trace()
        # log_add_to_cart(request.user.email, product.name, str(e))
        # log_add_to_cart(request.user.email, product.name)
        create_audit_log(f'{request.user.email} added {product.name} to cart.', request.user.email)
        response_data = {
                'id': str(cart_item.id),
                'cart_id': str(cart_item.cart_id),
                'product_id': str(cart_item.product_id),
                'quantity': cart_item.quantity,
                'products': []
        }
        response_data = {
            "data": response_data
        }

        return JSONResponse(response_data, status_code=201)
    except Exception as e:
        request.app.state.db.rollback()
        return JSONResponse(
            {'error': str(e)},
            status_code=500
        )
        
@requires('authenticated')
async def get_user_cart(request:Request):
    # try:
        services = CartServices(db=request.app.state.db)
        cart = services.get_or_create_cart(user_id=request.user.id)
        cart_items = services.get_cart_items(cart_id=cart.id)

        response_data = {
            'id': str(cart.id),
            'user_id': str(cart.user_id),
            'products': []
        }

        for cart_item in cart_items:
            response_data['products'].append({
                'id': str(cart_item.id),
                'cart_id': str(cart_item.cart_id),
                'product_id': str(cart_item.product_id),
                'quantity': cart_item.quantity
            })

        response_data = {
            "data": response_data
        }

        return JSONResponse(response_data, status_code=200)
    

    # except Exception as e:
    #     return JSONResponse(
    #         {'error': str(e)},
    #         status_code=500
    #     )
        