from database import engine, Base
from models import User
# Create all tables in the database
Base.metadata.create_all(bind=engine)