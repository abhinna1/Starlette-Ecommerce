from database import Base
from sqlalchemy import Column, Integer, ForeignKey, UUID, String
from sqlalchemy.orm import relationship
import uuid


class CartItems(Base):
    __tablename__ = 'cart_items'
    id = Column(UUID(), primary_key=True, index=True, unique=True, nullable=False, default=uuid.uuid4)
    cart_id = Column(UUID(), ForeignKey('carts.id'), nullable=False)
    product_id = Column(UUID(), ForeignKey('products.id'), nullable=False)
    quantity = Column(String(), nullable=False)
    cart = relationship("Cart", back_populates="cart_items")
    # cart = relationship("Cart", back_populates="cart_items")
    # product = relationship("Product", back_populates="cart_items")
    