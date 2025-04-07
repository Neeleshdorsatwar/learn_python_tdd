import unittest
from src.product_developement import ProductCatalog
from src.product import Product

class TestProductCatalog(unittest.TestCase):
    def setUp(self):
        self.catalog = ProductCatalog()
        self.test_product = Product(
            name="Test Product",
            sku="TP001",
            price=99.99,
            description="A test product",
            stock_quantity=10
        )
        self.another_product = Product(
            name="Another Test Product",
            sku="TP002",
            price=49.99,
            description="Another test product",
            stock_quantity=5
        )

    def tearDown(self):
        self.catalog = None
        self.test_product = None
        self.another_product = None

    def test_add_product(self):
        # Add the product to catalog
        self.catalog.add_product(self.test_product)
        
        # Get the list of products
        products = self.catalog.list_products()
        
        # Verify the product was added correctly
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0].name, "Test Product")
        self.assertEqual(products[0].sku, "TP001")
        self.assertEqual(products[0].price, 99.99)
        self.assertEqual(products[0].description, "A test product")
        self.assertEqual(products[0].stock_quantity, 10)

    def test_list_products_empty(self):
        # Get the list of products
        products = self.catalog.list_products()
        
        # Verify the catalog is empty
        self.assertEqual(len(products), 0)

    def test_remove_product(self):
        # Add products to catalog
        self.catalog.add_product(self.test_product)
        self.catalog.add_product(self.another_product)
        
        # Remove a product
        result = self.catalog.remove_product("TP001")
        
        # Verify removal was successful
        self.assertTrue(result)
        self.assertEqual(len(self.catalog.list_all_products()), 1)
        self.assertEqual(self.catalog.list_all_products()[0].sku, "TP002")

    def test_remove_product_not_found(self):
        # Try to remove non-existent product
        result = self.catalog.remove_product("NONEXISTENT")
        
        # Verify removal failed
        self.assertFalse(result)
        self.assertEqual(len(self.catalog.list_all_products()), 0)

    def test_search_by_name(self):
        # Add products to catalog
        self.catalog.add_product(self.test_product)
        self.catalog.add_product(self.another_product)
        
        # Search for products
        results = self.catalog.search_by_name("Test")
        
        # Verify search results
        self.assertEqual(len(results), 2)
        self.assertTrue(any(p.sku == "TP001" for p in results))
        self.assertTrue(any(p.sku == "TP002" for p in results))

    def test_search_by_name_case_insensitive(self):
        # Add product to catalog
        self.catalog.add_product(self.test_product)
        
        # Search with different case
        results = self.catalog.search_by_name("test")
        
        # Verify case-insensitive search
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].sku, "TP001")

    def test_search_by_sku(self):
        # Add product to catalog
        self.catalog.add_product(self.test_product)
        
        # Search by SKU
        result = self.catalog.search_by_sku("TP001")
        
        # Verify search result
        self.assertIsNotNone(result)
        self.assertEqual(result.name, "Test Product")
        self.assertEqual(result.sku, "TP001")

    def test_search_by_sku_not_found(self):
        # Search for non-existent SKU
        result = self.catalog.search_by_sku("NONEXISTENT")
        
        # Verify no result found
        self.assertIsNone(result)

    def test_list_all_products(self):
        # Add products to catalog
        self.catalog.add_product(self.test_product)
        self.catalog.add_product(self.another_product)
        
        # Get all products
        products = self.catalog.list_all_products()
        
        # Verify all products are returned
        self.assertEqual(len(products), 2)
        self.assertTrue(any(p.sku == "TP001" for p in products))
        self.assertTrue(any(p.sku == "TP002" for p in products))

if __name__ == '__main__':
    unittest.main()
