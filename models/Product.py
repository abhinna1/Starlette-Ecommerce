
from sqlalchemy import Column, String, Integer, DateTime, UUID
from database import Base
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB
import uuid

class Product(Base):
    __tablename__ = 'products'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, default=uuid.uuid4)
    name = Column(String(length=150), unique=True)
    description = Column(String(length=500))
    price = Column(Integer())
    quantity = Column(Integer(), default=0)
    image = Column(JSONB(), nullable=False, default=[])