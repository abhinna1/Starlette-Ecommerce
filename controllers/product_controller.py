from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.authentication import requires
from services.product_services import ProductServices
from abstracts.ProductAbstract import DatabaseProductAbstract
from starlette.authentication import requires

async def get_all_products(request: Request):
    db = request.app.state.db
    product_service = ProductServices(db)
    products = product_service.get_all_products()
    return JSONResponse(products)

async def get_product_by_id(request: Request):
    db = request.app.state.db
    product_service = ProductServices(db)
    product_id = request.path_params.get('product_id')
    product = product_service.get_product_by_id(product_id)
    return JSONResponse(product)

@requires(scopes=['authenticated', 'admin'])
async def create_product(request: Request):
    db = request.app.state.db
    try:
        product_service = ProductServices(db)
        data = await request.json()
        product = product_service.create_product(data)
        product = DatabaseProductAbstract(
            id=product.id,
            name=product.name,
            price=product.price,
            description=product.description,
            quantity= product.quantity,
            image=product.image,
        )
        product = product.dict()
        product['id'] = str(product['id'])
        return JSONResponse(
            product,
        )
    except Exception as e:
        return JSONResponse({'message': str(e)}, status_code=400)