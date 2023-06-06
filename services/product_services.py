from database import Base
from repositories.ProductRepository import ProductRepository
from models.Product import Product

class ProductServices:
    def __init__(self, db):
        self.product_repository = ProductRepository(db)
    
    def get_all_products(self):
        return self.product_repository.get_all_products()
    
    def get_product_by_id(self, product_id:str):
        return self.product_repository.get_product_by_id(product_id)
    
    def create_product(self, data:Product):
        product = self.product_repository.create_product(data)
        if not product:
            raise Exception("Product doesn't exist.")
        return product