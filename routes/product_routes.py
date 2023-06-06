from starlette.routing import Route
from controllers.product_controller import (
    get_all_products,
    get_product_by_id,
    create_product,
)
from routes.BaseRoute import BaseRoute

class ProductRoutes(BaseRoute):
    routes = [
        Route('/', endpoint=get_all_products, methods=['GET']),
        Route('/{product_id}', endpoint=get_product_by_id, methods=['GET']),
        Route('/', endpoint=create_product, methods=['POST']),
    ]