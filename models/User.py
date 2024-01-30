from sqlalchemy import Column, String, Enum, UUID, Integer
from database import Base
from commons.ENUMS import UserEnum
import uuid
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True, default=uuid.uuid4)
    username = Column(String(), unique=True)
    email = Column(String(), unique=True)
    password = Column(String())
    role = Column(Enum(UserEnum), default=UserEnum.USER)
    failed_login = Column(Integer(), default=0)
    
    
    