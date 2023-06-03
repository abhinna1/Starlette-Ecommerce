from sqlalchemy.orm import Session
from models.User import User
import bcrypt

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, username: str, email: str, password: str):
        user = User(username=username, email=email, password=password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_id(self, id: int):
        return self.db.query(User).filter(User.id == id).first()

    def get_user_by_username(self, username: str):
        return self.db.query(User).filter(User.username == username).first()

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()
    
    def compare_password_hash(self, email:str, password:str):
        """
            Compare if the hash of the input password is same as the stored password hash. 
        """
        user = self.get_user_by_email(email)
        return bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8'))