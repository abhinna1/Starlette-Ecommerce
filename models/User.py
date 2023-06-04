from sqlalchemy import Column, String, Integer, Enum
from database import Base
from commons.ENUMS import UserEnum

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    role = Column(Enum(UserEnum), default=UserEnum.USER)
