
from sqlalchemy import Column, String, Integer, DateTime, UUID, ForeignKey
from database import Base
from datetime import datetime
import uuid

class Review(Base):
    __tablename__ = 'review'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, default=uuid.uuid4, nullable=False)
    description = Column(String(length=500), nullable=False)
    product_id = Column(UUID(), ForeignKey('products.id'), nullable=False)
    user_id = Column(UUID(), ForeignKey('users.id'), nullable=False)