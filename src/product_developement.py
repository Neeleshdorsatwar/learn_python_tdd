from src.product import Product

# Create a product catalog
class ProductCatalog:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)

    def remove_product(self, sku):
        for product in self.products:
            if product.sku == sku:
                self.products.remove(product)
                return True
        return False

    def search_by_name(self, name):
        matching_products = []
        for product in self.products:
            if name.lower() in product.name.lower():
                matching_products.append(product)
        return matching_products

    def search_by_sku(self, sku):
        for product in self.products:
            if product.sku == sku:
                return product
        return None

    def list_all_products(self):
        return self.products

    def list_products(self):
        return self.products
