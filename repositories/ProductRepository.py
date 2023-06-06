
from models.Product import Product
from sqlalchemy.orm import Session
from abstracts.ProductAbstract import ProductAbstract

class ProductRepository:
    def __init__(self, db:Session):
        self.db = db

    def get_all_products(self):
        self.db.query(Product).all()
    
    def get_product_by_id(self, product_id:str):
        return self.db.query(Product).filter(Product.id == product_id).first()
    
    def create_product(self, data:dict):
        validated_data = ProductAbstract(**data)
        product = Product(**validated_data.dict())
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product