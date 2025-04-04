# Assignment 3: Product Catalog and Invoice System

---

# Objective

Your task is to design and implement a system that manages a **Product Catalog** and generates an **Invoice**. The system should allow users to add, view, and search products in a catalog and create invoices for customers by selecting products from the catalog. Each invoice will include product details, quantities, and the total cost.

---

## Requirements

### Part 1: Product Catalog

#### Product Class

Create a `Product` class with the following attributes:

- **name** (string): The name of the product.
- **sku** (string): The unique SKU (Stock Keeping Unit) for the product.
- **price** (float): The price of a single unit of the product.
- **description** (string, optional): A brief description of the product.
- **stock_quantity** (integer): The quantity of the product available in stock.

The class should have the following methods:

- **Constructor**: Initializes the product with its name, SKU, price, description, and stock quantity.
- **`__str__()` method**: Returns a string representation of the product in the following format:
    ```
    Product Name: <name>, SKU: <sku>, Price: $<price>, Stock: <stock_quantity>, Description: <description>
    ```
- **`update_stock(quantity)`**: Decreases the stock quantity of the product by the specified quantity (used when a product is purchased). Raises an error if the quantity to be deducted is greater than the available stock.

#### ProductCatalog Class

Create a `ProductCatalog` class that holds a collection of `Product` objects.

The class should have the following attributes:

- **products** (list): A list to store all the `Product` objects in the catalog.

The class should have the following methods:

- **`add_product(product)`**: Adds a `Product` object to the catalog.
- **`remove_product(sku)`**: Removes a product from the catalog by SKU.
- **`search_by_name(name)`**: Searches for products by name and returns a list of matching products.
- **`search_by_sku(sku)`**: Searches for a product by SKU and returns the matching product.
- **`list_all_products()`**: Returns a list of all products currently in the catalog.

---

### Part 2: Invoice Builder

#### Invoice Class

Create an `Invoice` class with the following attributes:

- **invoice_id** (string): A unique identifier for the invoice.
- **date** (string): The date of the invoice (use `YYYY-MM-DD` format).
- **customer_name** (string): The name of the customer.
- **products** (list): A list of products added to the invoice (with quantities).
- **total_amount** (float): The total cost of the products on the invoice.

The class should have the following methods:

- **Constructor**: Initializes the invoice with a unique invoice ID, the customer’s name, and the date.
- **`add_product_to_invoice(product, quantity)`**: Adds a product to the invoice with the specified quantity and updates the total cost. The `Product` object will be selected from the catalog, and the quantity should be checked against the product's available stock.
- **`generate_invoice()`**: Generates the invoice as a string displaying the product details (name, price, quantity), the total amount, and any additional details (e.g., invoice ID and date).
- **`calculate_total()`**: Calculates the total cost of the products in the invoice by multiplying the price of each product by its quantity.

#### InvoiceSystem Class

Create an `InvoiceSystem` class to manage the creation of invoices and the processing of orders.

The class should have the following methods:

- **`create_invoice(customer_name)`**: Creates a new invoice for a customer and assigns a unique invoice ID.
- **`list_invoices()`**: Lists all generated invoices with their details (invoice ID, customer name, total amount).
- **`search_invoice_by_id(invoice_id)`**: Searches for an invoice by its ID and returns the invoice details.
