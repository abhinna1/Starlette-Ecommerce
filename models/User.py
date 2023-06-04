from sqlalchemy import Column, String, Enum, UUID
from database import Base
from commons.ENUMS import UserEnum
import uuid

class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, default=uuid.uuid4)
    username = Column(String(), unique=True)
    email = Column(String(), unique=True)
    password = Column(String())
    role = Column(Enum(UserEnum), default=UserEnum.USER)
