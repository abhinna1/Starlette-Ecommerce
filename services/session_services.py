from models.UserSession import UserSession
from repositories.SessionRepository import SessionRepository
from repositories.UserRepository import UserRepository
from sqlalchemy.orm import Session

class SessionServices:
    def __init__(self, db:Session):
        self.session_repository = SessionRepository(db)
        self.user_repository = UserRepository(db)
        self.db = db
    
    def create_session(self, email:str, password:str) -> UserSession:
        user = self.user_repository.get_user_by_email(email)
        if not user:
            user.failed_login += 1
            self.db.commit()
            # self.db.save(user)
            raise Exception("User doesn't exist.")
        
        if not user.failed_login < 4:
            user.failed_login += 1
            self.db.commit()
            raise Exception("User is locked.")
            
        if not self.user_repository.compare_password_hash(email, password):
            user.failed_login += 1
            self.db.commit()
            # self.db.save(user)
            raise Exception("Password is incorrect.")
        
        user.failed_login = 0
        self.db.commit()
            
        return self.session_repository.create_session(user)

    def get_session_by_id(self, session_id:str) -> UserSession:
        return self.session_repository.get_session_by_id(session_id)
    
    def get_user_by_session_id(self, session_id:str):
        session = self.session_repository.get_session_by_id(session_id)
        return session.user
    
    # def delete_session(self, session:UserSession):
    #     self.session_repository.delete_session(session)
        