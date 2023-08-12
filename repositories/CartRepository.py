from datetime import datetime
from sqlalchemy.orm import Session
from abstracts.CartAbstract import CartAbstract, CartItemAbstract, DbCartItemAbstract
from models.Cart import Cart
from commons.ENUMS import CartStatusEnum
from models.Product import Product
from services.product_services import ProductServices
from models.CartItems import CartItems
from sqlalchemy import select, join
from uuid import UUID

class CartRepository:
    def __init__(self, db:Session):
        self.db = db
        self.product_services = ProductServices(db=db)


    def get_or_create_cart(self, user_id:UUID, product_id=None):
        cart = self.db.query(Cart).filter(
            Cart.user_id == user_id,
            Cart.status == CartStatusEnum.ACTIVE
        ).first()

        if not cart:
            validated_cart = CartAbstract(
                user_id = user_id,
                status = CartStatusEnum.ACTIVE,
                ordered_at = datetime.now()         
            )
            cart = Cart(
                **validated_cart.dict()
            )
            return cart
        return cart
    
    def get_cart_by_id(self, cart_id:UUID):
        cart = self.db.query(Cart).filter(
            Cart.id == cart_id,
            Cart.status == CartStatusEnum.ACTIVE
        ).first()
        return cart

    def cart_exists(self, cart_id:UUID):
        cart = self.db.query(Cart).filter(
            Cart.id == cart_id,
            Cart.status == CartStatusEnum.ACTIVE
        ).first()

        return cart is not None
    
    def get_cart_items(self, cart_id:UUID):
        cart_items = self.db.query(CartItems).filter(
            CartItems.cart_id == cart_id
        ).all()
        return cart_items
        
    
    def create_user_cart(self, user_id:UUID):
        cart = Cart(
            user_id = user_id,
            ordered_at = datetime.now(),
            status = CartStatusEnum.ACTIVE
        )
        self.db.add(cart)
        self.db.commit()
        self.db.refresh(cart)
        return cart
    
    def get_user_cart(self, user_id:UUID):
        cart = self.db.query(Cart).filter(
            Cart.user_id == user_id,
            Cart.status == CartStatusEnum.ACTIVE
        ).first()
        return cart
    
    def product_in_cart(self, cart_id:UUID, product_id:UUID):
        cart_item = self.db.query(CartItems).filter(
            CartItems.cart_id == cart_id,
            CartItems.product_id == product_id
        ).first()
        return cart_item is not None
    
    def update_cart_item(self, cart_id:UUID, product_id:UUID, quantity:int):
        cart_item = self.db.query(CartItems).filter(
            CartItems.cart_id == cart_id,
            CartItems.product_id == product_id
        ).first()
        cart_item.quantity = quantity
        self.db.commit()
        self.db.refresh(cart_item)
        return cart_item
    
    def add_product_to_cart(self, validated_cart_item:CartItemAbstract, cryptographer=None):
        cart_item = CartItems(
            **validated_cart_item.dict(),
        )
        cart_item.quantity = (cryptographer.encrypt(cart_item.quantity.encode('utf-8'))).decode('utf-8')
        # cart_item.quantity = (cart_item.quantity).decode('utf-8')
        cart = self.get_cart_by_id(cart_id=cart_item.cart_id)
        
        if not self.product_in_cart(
            cart_id=cart.id,
            product_id=cart_item.product_id
        ):
            # cart_item.product_id = cryptographer.encrypt(str(validated_cart_item.product_id).encode('utf-8'))
            self.db.add(cart_item)
            self.db.commit()
            self.db.refresh(cart_item)
            return cart_item

        updated_item = self.update_cart_item(
            cart_id = cart.id,
            product_id = cart_item.product_id,
            quantity=cart_item.quantity
        )
        updated_item.quantity = int((cryptographer.decrypt(updated_item.quantity)).decode('utf-8'))
        return updated_item


    def add_products_to_cart(self, validated_cart_items:list):
        items = []
        for item in validated_cart_items:
            self.add_product_to_cart(item)
        return items