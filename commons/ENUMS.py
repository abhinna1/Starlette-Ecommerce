import enum

class UserEnum(enum.Enum):
    USER = 'USER'
    ADMIN = 'ADMIN'

class CartStatusEnum(enum.Enum):
    ACTIVE = 'ACTIVE'
    ORDERED = 'ORDERED'
    CANCELLED = 'CANCELLED'