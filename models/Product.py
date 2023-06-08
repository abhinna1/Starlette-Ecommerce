
from sqlalchemy import Column, String, Integer, DateTime, UUID
from database import Base
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB
import uuid
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = 'products'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, default=uuid.uuid4, nullable=False)
    name = Column(String(length=150), nullable=False)
    description = Column(String(length=500), nullable=False)
    price = Column(Integer(), nullable=False)
    quantity = Column(Integer(), default=0, nullable=False)
    image = Column(JSONB(), nullable=True, default=[])