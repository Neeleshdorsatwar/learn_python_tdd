from datetime import datetime
from src.product import Product

class Invoice:
    def __init__(self, invoice_id: str, customer_name: str):
        self.invoice_id = invoice_id
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.customer_name = customer_name
        self.products = []  # List of tuples (product, quantity)
        self.total_amount = 0.0

    def add_product_to_invoice(self, product: Product, quantity: int) -> bool:
        """
        Adds a product to the invoice with the specified quantity.
        Returns True if successful, False if quantity exceeds stock.
        """
        if quantity <= 0:
            return False
            
        if quantity > product.stock_quantity:
            return False
            
        # Add product and quantity to the list
        self.products.append((product, quantity))
        
        # Update total amount
        self.calculate_total()
        
        return True

    def calculate_total(self) -> float:
        """
        Calculates the total cost of all products in the invoice.
        """
        self.total_amount = sum(product.price * quantity for product, quantity in self.products)
        return self.total_amount

    def generate_invoice(self) -> str:
        """
        Generates a formatted string representation of the invoice.
        """
        invoice_lines = [
            f"Invoice ID: {self.invoice_id}",
            f"Date: {self.date}",
            f"Customer: {self.customer_name}",
            "\nProducts:",
            "----------------------------------------",
        ]
        
        # Add product details
        for product, quantity in self.products:
            product_total = product.price * quantity
            invoice_lines.append(
                f"{product.name} (SKU: {product.sku})"
                f"\n  Quantity: {quantity}"
                f"\n  Price per unit: ${product.price:.2f}"
                f"\n  Total: ${product_total:.2f}"
            )
        
        # Add total amount
        invoice_lines.extend([
            "----------------------------------------",
            f"Total Amount: ${self.total_amount:.2f}"
        ])
        
        return "\n".join(invoice_lines)

    def __str__(self) -> str:
        return self.generate_invoice()
