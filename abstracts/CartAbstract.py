from pydantic import BaseModel
from uuid import UUID
from commons.ENUMS import CartStatusEnum
from datetime import datetime

class CartAbstract(BaseModel):
    user_id: UUID
    status: CartStatusEnum = CartStatusEnum.ACTIVE
    ordered_at: datetime = datetime.now()

class DbCartItemAbstract(BaseModel):
    id: UUID
    cart_id: UUID
    product_id: UUID
    quantity: int = 1

class CartItemAbstract(BaseModel):
    cart_id: UUID
    product_id: UUID
    quantity: str

class DbCartItemsAbstract(BaseModel):
    id: UUID
    cart_id: UUID
    product_id: UUID
    quantity: int = 1