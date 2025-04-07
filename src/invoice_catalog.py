from src.invoice import Invoice
import uuid

class InvoiceSystem:
    def __init__(self):
        self.invoices = {}  # Dictionary to store invoices with invoice_id as key

    def create_invoice(self, customer_name: str) -> Invoice:
        """
        Creates a new invoice for a customer and assigns a unique invoice ID.
        Returns the created invoice.
        """
        # Generate a unique invoice ID using UUID
        invoice_id = str(uuid.uuid4())
        
        # Create new invoice
        invoice = Invoice(invoice_id, customer_name)
        
        # Store the invoice
        self.invoices[invoice_id] = invoice
        
        return invoice

    def list_invoices(self) -> list:
        """
        Lists all generated invoices with their details.
        Returns a list of dictionaries containing invoice details.
        """
        invoice_list = []
        for invoice_id, invoice in self.invoices.items():
            invoice_details = {
                'invoice_id': invoice_id,
                'customer_name': invoice.customer_name,
                'date': invoice.date,
                'total_amount': invoice.total_amount
            }
            invoice_list.append(invoice_details)
        return invoice_list

    def search_invoice_by_id(self, invoice_id: str) -> dict:
        """
        Searches for an invoice by its ID and returns the invoice details.
        Returns None if invoice not found.
        """
        if invoice_id in self.invoices:
            invoice = self.invoices[invoice_id]
            return {
                'invoice_id': invoice_id,
                'customer_name': invoice.customer_name,
                'date': invoice.date,
                'total_amount': invoice.total_amount,
                'products': invoice.products
            }
        return None

