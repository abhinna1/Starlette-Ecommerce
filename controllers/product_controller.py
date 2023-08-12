from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.authentication import requires
from services.product_services import ProductServices
from abstracts.ProductAbstract import DatabaseProductAbstract
from starlette.authentication import requires
from models.Review import Review
from models.User import User

import json

async def get_all_products(request: Request):
    try:
        db = request.app.state.db
        product_service = ProductServices(db)
        products = product_service.get_all_products()
        products = [
            {
                "id": str(product.id),
                "name" : product.name,
                "description": product.description,
                "price": product.price,
                "quantity": product.quantity,
                # "image": product.image,
            }
            for product in products
        ]
        return JSONResponse({"data": products})
    except Exception as e:
        return JSONResponse({'message': str(e)}, status_code=400)

async def get_product_by_id(request: Request):
    try:
        db = request.app.state.db
        product_service = ProductServices(db)
        product_id = request.path_params.get('product_id')
        product = product_service.get_product_by_id(product_id)
        product = DatabaseProductAbstract(
            id=product.id,
            name=product.name,
            description=product.description,
            price=product.price,
            quantity=product.quantity,
            # image=product.image,
        )
        product = product.dict()
        product['id'] = str(product['id'])        
        return JSONResponse(product)
    except Exception as e:
        return JSONResponse({'message': str(e)}, status_code=400)

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
            # image=product.image,
        )
        product = product.dict()
        product['id'] = str(product['id'])
        return JSONResponse(
            product,
        )
    except Exception as e:
        return JSONResponse({'message': str(e)}, status_code=400)
    
@requires('authenticated')
async def add_review(request):
    try:
        data = await request.json()
        description = data['description']
        product_id = request.path_params.get('product_id')
        user_id = request.user.id
        


        review = Review(
            description=description,
            product_id=product_id,
            user_id=user_id
        )
        request.app.state.db.add(review)
        request.app.state.db.commit()

        return JSONResponse({'message': 'Review added successfully'}, status_code=201)
    except Exception as e:
        request.app.state.db.rollback()
        return JSONResponse({'message': str(e)}, status_code=500)
    
async def get_product_reviews(request):
    try:
        product_id = request.path_params.get('product_id')
        
        reviews = request.app.state.db.query(Review).filter(Review.product_id == product_id).all()
        reviews = [{
            "id": str(review.id),
            "description": review.description,
            "added_by_username": str((request.app.state.db.query(User).filter(User.id ==review.user_id).first()).username),
            "added_by_email": str((request.app.state.db.query(User).filter(User.id ==review.user_id).first()).email),
            } for review in reviews
        ]
        
        return JSONResponse({'message': 'Review added successfully', 'data': reviews}, status_code=200)
    except Exception as e:
        request.app.state.db.rollback()
        return JSONResponse({'message': str(e)}, status_code=500)