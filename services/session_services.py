from models.UserSession import UserSession
from repositories.SessionRepository import SessionRepository
from repositories.UserRepository import UserRepository
from sqlalchemy.orm import Session

class SessionServices:
    def __init__(self, db:Session):
        self.session_repository = SessionRepository(db)
        self.user_repository = UserRepository(db)
        
    
    def create_session(self, email:str, password:str) -> UserSession:
        user = self.user_repository.get_user_by_email(email)
        if not user:
            raise Exception("User doesn't exist.")
        if not self.user_repository.compare_password_hash(email, password):
            raise Exception("Password is incorrect.")
        return self.session_repository.create_session(user)