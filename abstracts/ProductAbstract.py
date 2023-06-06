from pydantic import BaseModel
import uuid
class ProductAbstract(BaseModel):
    name:str
    description:str
    price:int
    quantity:int
    image:list = []

class DatabaseProductAbstract(BaseModel):
    id:uuid.UUID
    name:str
    description:str
    price:int
    quantity:int
    image:list = []
