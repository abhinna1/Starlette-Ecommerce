from starlette.requests import Request
from abstracts.CartAbstract import CartItemAbstract, DbCartItemAbstract
from services.cart_services import CartServices
from starlette.authentication import requires
from starlette.responses import JSONResponse
from starlette import status

@requires('authenticated')
async def add_product_to_cart(request:Request):
    try:
        data = await request.json()
        services = CartServices(db=request.app.state.db)
        cart = services.get_or_create_cart(user_id=request.user.id)

        product_id = data.get('product')
        quantity = data.get('quantity', 1)
        
        if quantity == 0:
            return JSONResponse({"message": "Quantity must be greater than 0."}, status_code=status.HTTP_400_BAD_REQUEST)
        
        cart_item = services.add_product_to_cart(
            cart_id = cart.id,
            product_id = product_id,
            quantity = quantity,
            user_id=request.user.id
        )
        
        if not cart_item:
            return JSONResponse({"message": "Product removed from cart."})
        

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
        return JSONResponse(
            {'error': str(e)},
            status_code=500
        )