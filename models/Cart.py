from sqlalchemy.types import Boolean, DateTime, Integer, String, Enum, UUID
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from commons.ENUMS import CartStatusEnum
import uuid

class Cart(Base):
    __tablename__ = 'carts'
    id = Column(UUID(), primary_key=True, index=True, unique=True, nullable=False, default=uuid.uuid4)
    user_id = Column(Integer(), ForeignKey('users.id'), nullable=False)
    ordered_at = Column(DateTime(), nullable=True)
    status = Column(Enum(CartStatusEnum), default=CartStatusEnum.ACTIVE)
    # user = relationship("User")
    cart_items = relationship("CartItems", back_populates="cart")