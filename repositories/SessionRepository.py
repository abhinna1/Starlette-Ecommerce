from sqlalchemy.orm import Session
from models.User import User
from models.UserSession import UserSession
class SessionRepository:
    def __init__(self, db:Session):
        self.db = db
    
    def create_session(self, user:User):
        session = UserSession(user_id=user.id)
        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)
        return session
    
    def get_session_by_id(self, session_id:str):
        return self.db.query(UserSession).filter(UserSession.id == session_id).first()
    