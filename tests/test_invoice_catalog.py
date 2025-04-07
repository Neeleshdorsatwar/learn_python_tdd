import unittest
from src.invoice_catalog import InvoiceSystem
from src.product import Product

class TestInvoiceSystem(unittest.TestCase):
    def setUp(self):
        self.invoice_system = InvoiceSystem()
        self.test_product = Product(
            name="Test Product",
            sku="TP001",
            price=99.99,
            description="A test product",
            stock_quantity=10
        )

    def tearDown(self):
        self.invoice_system = None
        self.test_product = None

    def test_create_invoice(self):
        """Test creating a new invoice"""
        # Create a new invoice
        invoice = self.invoice_system.create_invoice("John Doe")
        
        # Verify invoice was created with correct details
        self.assertEqual(invoice.customer_name, "John Doe")
        self.assertIsNotNone(invoice.invoice_id)
        self.assertEqual(len(invoice.products), 0)
        self.assertEqual(invoice.total_amount, 0.0)
        
        # Verify invoice was stored in the system
        self.assertEqual(len(self.invoice_system.invoices), 1)
        self.assertIn(invoice.invoice_id, self.invoice_system.invoices)

    def test_create_multiple_invoices(self):
        """Test creating multiple invoices"""
        # Create multiple invoices
        invoice1 = self.invoice_system.create_invoice("John Doe")
        invoice2 = self.invoice_system.create_invoice("Jane Smith")
        
        # Verify both invoices were created and stored
        self.assertEqual(len(self.invoice_system.invoices), 2)
        self.assertIn(invoice1.invoice_id, self.invoice_system.invoices)
        self.assertIn(invoice2.invoice_id, self.invoice_system.invoices)
        
        # Verify unique invoice IDs
        self.assertNotEqual(invoice1.invoice_id, invoice2.invoice_id)

    def test_list_invoices(self):
        """Test listing all invoices"""
        # Create some invoices
        invoice1 = self.invoice_system.create_invoice("John Doe")
        invoice2 = self.invoice_system.create_invoice("Jane Smith")
        
        # Add products to invoices
        invoice1.add_product_to_invoice(self.test_product, 2)
        invoice2.add_product_to_invoice(self.test_product, 1)
        
        # Get list of invoices
        invoice_list = self.invoice_system.list_invoices()
        
        # Verify list contains correct number of invoices
        self.assertEqual(len(invoice_list), 2)
        
        # Verify invoice details
        for invoice_details in invoice_list:
            self.assertIn('invoice_id', invoice_details)
            self.assertIn('customer_name', invoice_details)
            self.assertIn('date', invoice_details)
            self.assertIn('total_amount', invoice_details)
            
            # Verify total amounts are correct
            if invoice_details['customer_name'] == "John Doe":
                self.assertEqual(invoice_details['total_amount'], 199.98)  # 2 * 99.99
            else:
                self.assertEqual(invoice_details['total_amount'], 99.99)  # 1 * 99.99

    def test_search_invoice_by_id(self):
        """Test searching for an invoice by ID"""
        # Create an invoice
        invoice = self.invoice_system.create_invoice("John Doe")
        invoice.add_product_to_invoice(self.test_product, 2)
        
        # Search for the invoice
        invoice_details = self.invoice_system.search_invoice_by_id(invoice.invoice_id)
        
        # Verify invoice details
        self.assertIsNotNone(invoice_details)
        self.assertEqual(invoice_details['invoice_id'], invoice.invoice_id)
        self.assertEqual(invoice_details['customer_name'], "John Doe")
        self.assertEqual(invoice_details['total_amount'], 199.98)  # 2 * 99.99
        self.assertEqual(len(invoice_details['products']), 1)

    def test_search_invoice_by_id_not_found(self):
        """Test searching for a non-existent invoice"""
        # Search for non-existent invoice
        invoice_details = self.invoice_system.search_invoice_by_id("NONEXISTENT")
        
        # Verify no invoice was found
        self.assertIsNone(invoice_details)

if __name__ == '__main__':
    unittest.main() 