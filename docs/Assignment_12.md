### Problem Statement: Food Delivery Service Management System

#### Objective:
Design and implement a **Food Delivery Service Management System** using Object-Oriented Programming (OOP) principles. The system will facilitate the management of food orders, customer information, restaurant details, and delivery personnel. It will handle placing orders, processing payments, assigning delivery tasks, and tracking the status of orders. The system should also allow for managing different restaurants, menu items, and provide an interface to manage customers and deliveries efficiently.

#### Requirements:

### 1. **Class Definitions**

#### 1.1 **Customer Class**
- **Attributes:**
  - `customer_id` (string): A unique identifier for the customer (e.g., "CUST001").
  - `name` (string): The name of the customer.
  - `email` (string): The customer's email address.
  - `address` (string): The delivery address of the customer.
  - `phone_number` (string): The customer's contact number.
  - `order_history` (list): A list of orders placed by the customer (Order objects).

- **Methods:**
  - **Constructor (`__init__`)**: Initializes the customer with `customer_id`, `name`, `email`, `address`, `phone_number`, and an empty list for `order_history`.
  - **`place_order(order)`**: Places a new order, adding it to the `order_history`.
  - **`view_order_history()`**: Displays a list of past orders made by the customer.
  - **`__str__()`**: Returns a string representation of the customer with basic details.

#### 1.2 **Restaurant Class**
- **Attributes:**
  - `restaurant_id` (string): A unique identifier for the restaurant (e.g., "RESTAURANT001").
  - `name` (string): The name of the restaurant.
  - `location` (string): The address of the restaurant.
  - `menu_items` (list): A list of food items available in the restaurant’s menu (FoodItem objects).
  
- **Methods:**
  - **Constructor (`__init__`)**: Initializes the restaurant with `restaurant_id`, `name`, `location`, and an empty list for `menu_items`.
  - **`add_menu_item(food_item)`**: Adds a new food item to the restaurant's menu.
  - **`remove_menu_item(food_item_id)`**: Removes a menu item based on its unique identifier.
  - **`view_menu()`**: Displays a list of all food items available on the restaurant's menu.
  - **`__str__()`**: Returns a string representation of the restaurant, including its name and location.

#### 1.3 **FoodItem Class**
- **Attributes:**
  - `food_id` (string): A unique identifier for the food item (e.g., "FOOD001").
  - `name` (string): The name of the food item (e.g., "Pizza", "Burger").
  - `price` (float): The price of the food item.
  - `category` (string): The type of food (e.g., "Pizza", "Beverage", "Dessert").

- **Methods:**
  - **Constructor (`__init__`)**: Initializes the food item with `food_id`, `name`, `price`, and `category`.
  - **`__str__()`**: Returns a string representation of the food item with its name, price, and category.

#### 1.4 **Order Class**
- **Attributes:**
  - `order_id` (string): A unique identifier for the order (e.g., "ORDER001").
  - `customer` (Customer object): The customer who placed the order.
  - `restaurant` (Restaurant object): The restaurant from which the order was placed.
  - `food_items` (list): A list of food items in the order (FoodItem objects).
  - `total_price` (float): The total cost of the order.
  - `status` (string): The status of the order (e.g., "Pending", "In Progress", "Delivered").
  - `delivery_person` (DeliveryPerson object): The delivery person assigned to the order.

- **Methods:**
  - **Constructor (`__init__`)**: Initializes the order with `order_id`, `customer`, `restaurant`, `food_items`, `total_price`, `status`, and `delivery_person`.
  - **`calculate_total()`**: Calculates the total price of the order based on the food items.
  - **`update_status(status)`**: Updates the status of the order (e.g., from "Pending" to "In Progress").
  - **`assign_delivery_person(delivery_person)`**: Assigns a delivery person to the order.
  - **`__str__()`**: Returns a string representation of the order, including the customer, restaurant, food items, total price, and order status.

#### 1.5 **DeliveryPerson Class**
- **Attributes:**
  - `delivery_person_id` (string): A unique identifier for the delivery person (e.g., "DEL001").
  - `name` (string): The name of the delivery person.
  - `phone_number` (string): The contact number of the delivery person.
  - `assigned_orders` (list): A list of orders assigned to the delivery person (Order objects).

- **Methods:**
  - **Constructor (`__init__`)**: Initializes the delivery person with `delivery_person_id`, `name`, `phone_number`, and an empty list for `assigned_orders`.
  - **`assign_order(order)`**: Assigns an order to the delivery person, adding it to the `assigned_orders` list.
  - **`view_assigned_orders()`**: Displays a list of orders currently assigned to the delivery person.
  - **`__str__()`**: Returns a string representation of the delivery person, including their name and contact information.

#### 1.6 **FoodDeliveryService Class**
- **Attributes:**
  - `customers` (list): A list of all customers using the service.
  - `restaurants` (list): A list of all registered restaurants.
  - `orders` (list): A list of all orders placed through the service.
  - `delivery_personnel` (list): A list of all delivery persons.

- **Methods:**
  - **Constructor (`__init__`)**: Initializes the service with empty lists for `customers`, `restaurants`, `orders`, and `delivery_personnel`.
  - **`register_customer(customer)`**: Registers a new customer in the service.
  - **`register_restaurant(restaurant)`**: Registers a new restaurant in the system.
  - **`place_order(customer_id, restaurant_id, food_items)`**: Places a new order for a customer from a specific restaurant.
  - **`assign_delivery_person(order_id, delivery_person_id)`**: Assigns a delivery person to an order.
  - **`view_all_orders()`**: Displays a list of all orders placed through the service.
  - **`__str__()`**: Returns a summary of all registered customers, restaurants, and orders.

### 2. **Features**

#### 2.1 **Customer Order Management**
- Customers can place orders from different restaurants, view order history, and check the status of current orders.
- Orders contain multiple food items from the restaurant's menu, and each order has a total price.
  
#### 2.2 **Restaurant Menu Management**
- Restaurants can add and remove menu items (food items), and customers can choose from these items to build their orders.

#### 2.3 **Delivery Assignment**
- Delivery personnel can be assigned to specific orders, and their progress in delivering the order can be monitored.
  
#### 2.4 **Order Status Updates**
- Orders can have different statuses such as "Pending", "In Progress", and "Delivered", which are updated as the order moves through the system.

#### 2.5 **Payment and Pricing**
- Each order's total price is calculated based on the food items selected. Payment methods can be simulated through a simple interface (e.g., “Cash on Delivery” or “Online Payment”).

### 3. **Sample Usage**

```python
# Create a food delivery service
service = FoodDeliveryService()

# Register a customer
customer = Customer("CUST001", "John Doe", "john@example.com", "123 Elm St", "555-1234")
service.register_customer(customer)

# Register a restaurant
restaurant = Restaurant("RESTAURANT001", "Pizza Palace", "456 Pizza Lane")
service.register_restaurant(restaurant)

# Add menu items to the restaurant
pizza = FoodItem("FOOD001", "Pepperoni Pizza", 12.99, "Pizza")
burger = FoodItem("FOOD002", "Cheeseburger", 8.99, "Burger")
restaurant.add_menu_item(pizza)
restaurant.add_menu_item(burger)

# Customer places an order
order_items = [pizza, burger]
order = service.place_order("CUST001", "RESTAURANT001", order_items)

# Assign a delivery person to the order
delivery_person = DeliveryPerson("DEL001", "Alice", "555-5678")
service.assign_delivery_person(order.order_id, delivery_person.delivery_person_id)

# View the order and its status
print(order)

# View all orders in the system
service.view_all_orders()
```

### 4. **Expected Output**

```
Order ID: ORDER001, Customer: John Doe, Restaurant: Pizza Palace
Food Items:
- Pepperoni Pizza, $12.99
- Cheeseburger, $8.99
Total Price: $21.98
Status: Pending

All orders in the system:
1. ORDER001 - Status: Pending, Customer: John Doe, Restaurant: Pizza Palace
```

### 5. **Constraints:**
- The system should handle multiple customers, restaurants, and orders.
- Food items must be priced and categorized correctly.
- Orders should have unique order IDs.
- Delivery personnel should be able to manage multiple assigned orders at once.
- The system should allow for updates to the order status as it progresses through the delivery process.

---

This **Food Delivery Service Management System** provides an efficient way to manage customers, restaurants, and deliveries. It tracks the lifecycle of each order from placement to delivery, enabling seamless food ordering and delivery operations.