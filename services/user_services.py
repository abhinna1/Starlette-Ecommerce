from repositories.UserRepository import UserRepository
from sqlalchemy.orm import Session
from models.User import User

class UserServices:
    def __init__(self, db:Session):
        self.user_repository = UserRepository(db)

    def create_user(self, username: str, email: str, password: str, cfm_password:str)-> User:
        if password != cfm_password:
            raise Exception('Password and confirm password are not match')
        return self.user_repository.create_user(username, email, password)
    