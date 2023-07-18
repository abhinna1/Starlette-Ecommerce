from abstracts.CartAbstract import CartItemAbstract
from database import Base
from repositories.ProductRepository import ProductRepository
from repositories.CartRepository import CartRepository
from models.Product import Product
from uuid import UUID

class CartServices:
    def __init__(self, db):
        self.cart_repository = CartRepository(db)
        self.product_repository = ProductRepository(db)
    
    def get_or_create_cart(self, user_id:UUID, product_id:UUID=None):
        return self.cart_repository.get_or_create_cart(
            user_id=user_id,
            product_id=product_id
        )
    
    def add_product_to_cart(self, cart_id:UUID, product_id:UUID, quantity:int=1, user_id:UUID=None):
        
        product = self.product_repository.get_product_by_id(
            product_id=product_id
        )
        if not product:
            raise Exception('Product not found')
        if not self.cart_repository.cart_exists(cart_id=cart_id):
            self.cart_repository.create_user_cart(user_id=user_id)

        validated_cart_item = CartItemAbstract(
            cart_id=cart_id,
            product_id=product_id,
            quantity=quantity
        )

        return self.cart_repository.add_product_to_cart(
            validated_cart_item
        )