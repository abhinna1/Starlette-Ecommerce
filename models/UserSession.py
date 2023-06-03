from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, UUID
from sqlalchemy.orm import relationship
from datetime import datetime, timedelta
from database import Base
import uuid
import dotenv
import os

dotenv.load_dotenv()

session_life = int(os.getenv("SESSION_LIFE"))
class UserSession(Base):
    __tablename__ = 'sessions'
    id = Column(UUID, primary_key=True, index=True, default=str(uuid.uuid4()))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, default=datetime.utcnow() + timedelta(days=session_life))
    is_expired = Column(Boolean, default=False)

    def is_active(self):
        """
        Checks if the session is active or valid based on the expiration time.
        Returns True if the session is active, False otherwise.
        """
        return datetime.utcnow() < self.expires_at and not self.is_expired

    def force_expire(self):
        """
        Forces the session to expire immediately by setting the 'expired' flag to True.
        """
        self.expired = True