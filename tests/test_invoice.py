import unittest
from datetime import datetime
from src.invoice import Invoice
from src.product import Product

class TestInvoice(unittest.TestCase):
    def setUp(self):
        self.test_product = Product(
            name="Test Product",
            sku="TP001",
            price=99.99,
            description="A test product",
            stock_quantity=10
        )
        self.another_product = Product(
            name="Another Product",
            sku="TP002",
            price=49.99,
            description="Another test product",
            stock_quantity=5
        )
        self.invoice = Invoice("INV001", "John Doe")

    def tearDown(self):
        self.invoice = None
        self.test_product = None
        self.another_product = None

    def test_initialization(self):
        """Test the initialization of Invoice attributes"""
        self.assertEqual(self.invoice.invoice_id, "INV001")
        self.assertEqual(self.invoice.customer_name, "John Doe")
        self.assertEqual(self.invoice.products, [])
        self.assertEqual(self.invoice.total_amount, 0.0)
        
        # Check date format
        try:
            datetime.strptime(self.invoice.date, "%Y-%m-%d")
        except ValueError:
            self.fail("Date is not in YYYY-MM-DD format")

    def test_add_product_to_invoice(self):
        """Test adding products to invoice"""
        # Test successful addition
        result = self.invoice.add_product_to_invoice(self.test_product, 2)
        self.assertTrue(result)
        self.assertEqual(len(self.invoice.products), 1)
        self.assertEqual(self.invoice.products[0][0], self.test_product)
        self.assertEqual(self.invoice.products[0][1], 2)

        # Test adding another product
        result = self.invoice.add_product_to_invoice(self.another_product, 1)
        self.assertTrue(result)
        self.assertEqual(len(self.invoice.products), 2)

    def test_add_product_to_invoice_invalid_quantity(self):
        """Test adding products with invalid quantities"""
        # Test zero quantity
        result = self.invoice.add_product_to_invoice(self.test_product, 0)
        self.assertFalse(result)
        self.assertEqual(len(self.invoice.products), 0)

        # Test negative quantity
        result = self.invoice.add_product_to_invoice(self.test_product, -1)
        self.assertFalse(result)
        self.assertEqual(len(self.invoice.products), 0)

        # Test quantity exceeding stock
        result = self.invoice.add_product_to_invoice(self.test_product, 11)
        self.assertFalse(result)
        self.assertEqual(len(self.invoice.products), 0)

    def test_calculate_total(self):
        """Test total calculation"""
        # Add products
        self.invoice.add_product_to_invoice(self.test_product, 2)  # 2 * 99.99 = 199.98
        self.invoice.add_product_to_invoice(self.another_product, 1)  # 1 * 49.99 = 49.99
        
        # Calculate total
        total = self.invoice.calculate_total()
        
        # Verify total
        expected_total = (2 * 99.99) + (1 * 49.99)
        self.assertEqual(total, expected_total)
        self.assertEqual(self.invoice.total_amount, expected_total)

    def test_generate_invoice(self):
        """Test invoice generation"""
        # Add products
        self.invoice.add_product_to_invoice(self.test_product, 2)
        self.invoice.add_product_to_invoice(self.another_product, 1)
        
        # Generate invoice
        invoice_text = self.invoice.generate_invoice()
        
        # Verify invoice contains all required information
        self.assertIn("INV001", invoice_text)
        self.assertIn("John Doe", invoice_text)
        self.assertIn("Test Product", invoice_text)
        self.assertIn("Another Product", invoice_text)
        self.assertIn("$99.99", invoice_text)
        self.assertIn("$49.99", invoice_text)
        self.assertIn("Quantity: 2", invoice_text)
        self.assertIn("Quantity: 1", invoice_text)
        self.assertIn("Total Amount", invoice_text)

    def test_str_method(self):
        """Test string representation of invoice"""
        # Add a product
        self.invoice.add_product_to_invoice(self.test_product, 1)
        
        # Get string representation
        invoice_str = str(self.invoice)
        
        # Verify it's the same as generate_invoice
        self.assertEqual(invoice_str, self.invoice.generate_invoice())

if __name__ == '__main__':
    unittest.main()
