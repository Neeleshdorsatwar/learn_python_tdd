class Product:
    def __init__(self, name, sku, price, description, stock_quantity):
        self.name = name
        self.sku = sku
        self.price = price
        self.description = description
        self.stock_quantity = stock_quantity

    def __repr__(self):
        return f"Product(name={self.name}, sku={self.sku}, price={self.price}, description={self.description}, stock_quantity={self.stock_quantity})"

    def to_string(self):
        return f"Name: {self.name}, SKU: {self.sku}, Price: {self.price}, Description: {self.description}, Stock Quantity: {self.stock_quantity}"