
from sqlalchemy import Column, String, Integer, DateTime, UUID, ForeignKey
from database import Base
from datetime import datetime
import uuid

class AuditLog(Base):
    __tablename__ = 'audit_log'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, default=uuid.uuid4, nullable=False)
    message = Column(String(length=500), nullable=False)
    created_by = Column(String(length=255), nullable=True)
    created_at = Column(DateTime(), default=datetime.now(), nullable=False)