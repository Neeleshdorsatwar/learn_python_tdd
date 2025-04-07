import unittest
from src.product import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product(
            name="Laptop",
            sku="12345",
            price=999.99,
            description="A high-performance laptop",
            stock_quantity=10
        )

    def test_product_initialization(self):
        self.assertEqual(self.product.name, "Laptop")
        self.assertEqual(self.product.sku, "12345")
        self.assertEqual(self.product.price, 999.99)
        self.assertEqual(self.product.description, "A high-performance laptop")
        self.assertEqual(self.product.stock_quantity, 10)

    def test_product_repr(self):
        expected_repr = "Product(name=Laptop, sku=12345, price=999.99, description=A high-performance laptop, stock_quantity=10)"
        self.assertEqual(repr(self.product), expected_repr)

    def test_product_to_string(self):
        expected_string = "Name: Laptop, SKU: 12345, Price: 999.99, Description: A high-performance laptop, Stock Quantity: 10"
        self.assertEqual(self.product.to_string(), expected_string)

if __name__ == "__main__":
    unittest.main()
 

