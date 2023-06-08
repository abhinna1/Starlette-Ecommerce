from starlette.requests import Request
from abstracts.CartAbstract import CartItemAbstract, DbCartItemAbstract
from services.cart_services import CartServices
from starlette.authentication import requires
from starlette.responses import JSONResponse

@requires('authenticated')
async def add_product_to_cart(request:Request):
    try:
        data = await request.json()
        services = CartServices(db=request.app.state.db)
        cart = services.get_or_create_cart(user_id=request.user.id)

        product_id = data.get('product_id')
        quantity = data.get('quantity', 1)
        
        cart_item = services.add_product_to_cart(
            cart_id = cart.id,
            product_id = product_id,
            quantity = quantity,
            user_id=request.user.id
        )

        response_data = {
                'id': str(cart_item.id),
                'cart_id': str(cart_item.cart_id),
                'product_id': str(cart_item.product_id),
                'quantity': cart_item.quantity
        }
        response_data = {
            "data": response_data
        }

        return JSONResponse(response_data, status_code=201)
    except Exception as e:
        return JSONResponse(
            {'error': str(e)},
            status_code=500
        )