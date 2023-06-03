from repositories.UserRepository import UserRepository
from sqlalchemy.orm import Session
from models.User import User
from helpers.auth_helpers import verify_password_strength, hash_password, check_common_password
class UserServices:
    def __init__(self, db:Session):
        self.user_repository = UserRepository(db)

    def create_user(self, username: str, email: str, password: str, cfm_password:str)-> User:
        if password != cfm_password:
            raise Exception('Password and confirm password are not match')
        if self.user_repository.get_user_by_username(username):
            raise Exception('Username already exists')
        if self.user_repository.get_user_by_email(email):
            raise Exception('Email already exists')
        
        if check_common_password(password):
            raise Exception('Password is too common.')
        if not verify_password_strength(password):
            raise Exception('Password is too weak')
        
        password = hash_password(password)

        return self.user_repository.create_user(username, email, password)