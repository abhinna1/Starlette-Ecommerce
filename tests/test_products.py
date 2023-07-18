from unittest import IsolatedAsyncioTestCase, TestCase
from repositories.ProductRepository import ProductRepository
from services.product_services import ProductServices
from database import SessionLocal

class TestProductRepository(TestCase):
    db = SessionLocal()
    repository = ProductRepository(db=db)
    
    def test_repository_initialization(self):
        print(self.repository)
        db = SessionLocal()
        repository = ProductRepository(db=db)
        self.assertEqual(type(self.repository), type(repository))
    
    def test_repository_get_all_products(self):
        products = self.repository.get_all_products()
        print(products[0].__dict__)
        self.assertEqual(type(products), list)
        
class TestProductServices(TestCase):
    db = SessionLocal()
    services = ProductServices(db)