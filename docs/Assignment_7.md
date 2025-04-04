# Assignment 7: Hotel Reservation and Room Availability Management System

## Objective
Design and implement a Hotel Reservation and Room Availability Management System using Object-Oriented Programming (OOP) principles. This system will allow hotel staff to manage room availability, process reservations, check-in and check-out guests, and handle payments. Customers should be able to view available rooms, make reservations, and track their booking status.

---

## Requirements

### 1. Class Definitions

#### 1.1 Room Class

**Attributes:**
- `room_number` (string): A unique identifier for each room (e.g., "101", "102", etc.).
- `room_type` (string): The type of room (e.g., "Single", "Double", "Suite").
- `price_per_night` (float): The price of the room per night.
- `availability` (bool): Indicates if the room is available for booking (`True` if available, `False` if booked).

**Methods:**
- **Constructor (`__init__`)**: Initializes the room with the given `room_number`, `room_type`, `price_per_night`, and `availability`.
- **`book_room()`**: Marks the room as booked and updates its availability status.
- **`cancel_booking()`**: Cancels the booking and updates the availability to `True`.
- **`__str__()`**: Returns a string representation of the room in the format:
    ```
    Room Number: <room_number>, Type: <room_type>, Price per Night: $<price_per_night>, Availability: <availability>
    ```

#### 1.2 Customer Class

**Attributes:**
- `customer_name` (string): The name of the customer.
- `customer_id` (string): A unique identifier for the customer (e.g., "CUST001").
- `reservations` (list): A list of reservations made by the customer. Each reservation is an instance of the `Reservation` class.

**Methods:**
- **Constructor (`__init__`)**: Initializes the customer with their `customer_name` and `customer_id`.
- **`make_reservation(room, check_in_date, check_out_date)`**: Allows the customer to make a reservation if the room is available. It creates a `Reservation` object and adds it to the customer's reservations list.
- **`cancel_reservation(reservation_id)`**: Allows the customer to cancel an existing reservation by its reservation ID.
- **`view_reservations()`**: Displays a list of the customer's reservations, showing room details and reservation dates.

#### 1.3 Reservation Class

**Attributes:**
- `reservation_id` (string): A unique identifier for the reservation.
- `room` (Room): The room associated with the reservation.
- `customer` (Customer): The customer who made the reservation.
- `check_in_date` (string): The date of check-in (e.g., "2025-05-01").
- `check_out_date` (string): The date of check-out (e.g., "2025-05-05").
- `total_cost` (float): The total cost of the reservation, calculated based on the room price and number of nights.

**Methods:**
- **Constructor (`__init__`)**: Initializes the reservation with the `reservation_id`, `room`, `customer`, `check_in_date`, `check_out_date`, and calculates the `total_cost`.
- **`calculate_total_cost()`**: Calculates the total cost of the reservation based on the room price and number of nights.
- **`__str__()`**: Returns a string representation of the reservation in the format:
    ```
    Reservation ID: <reservation_id>, Room: <room_number>, Customer: <customer_name>, Check-in: <check_in_date>, Check-out: <check_out_date>, Total Cost: $<total_cost>
    ```

#### 1.4 Hotel Class

**Attributes:**
- `hotel_name` (string): The name of the hotel.
- `rooms` (list): A list of all rooms in the hotel (each room is an instance of the `Room` class).
- `customers` (list): A list of all customers who have made reservations at the hotel.

**Methods:**
- **Constructor (`__init__`)**: Initializes the hotel with its `hotel_name` and an empty list of rooms and customers.
- **`add_room(room)`**: Adds a new room to the hotel.
- **`get_available_rooms()`**: Returns a list of all rooms that are currently available for booking.
- **`view_all_rooms()`**: Displays all rooms in the hotel, including their availability.
- **`add_customer(customer)`**: Adds a customer to the hotel's customer list.
- **`view_customer_reservations(customer_id)`**: Displays a customer's reservations based on their `customer_id`.

---

## 2. Features

### 2.1 Room Management
- The hotel should be able to manage a list of rooms with different room types (e.g., Single, Double, Suite) and prices.
- Rooms should have availability status, and when a reservation is made, the availability of the room should be updated.

### 2.2 Reservation Management
- Customers should be able to make reservations for available rooms by providing check-in and check-out dates.
- Reservations should be assigned a unique reservation ID and should include room details and the total cost.
- Customers should be able to cancel a reservation, which will update the availability of the room.

### 2.3 Pricing and Payment
- The total cost of a reservation should be calculated based on the number of nights and the price per night of the room.
- Implement payment processing by assuming the payment is made at the time of reservation.

### 2.4 Customer Management
- The hotel should maintain a list of customers who have made reservations.
- The system should allow customers to view their reservations and cancel them if necessary.

---

## 3. Sample Usage

```python
# Create a hotel instance
hotel = Hotel("Sunset Resort")

# Add rooms to the hotel
room1 = Room("101", "Single", 100)
room2 = Room("102", "Double", 150)
room3 = Room("103", "Suite", 250)

hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)

# Create customer instances
customer1 = Customer("Alice", "CUST001")
customer2 = Customer("Bob", "CUST002")

# Add customers to the hotel
hotel.add_customer(customer1)
hotel.add_customer(customer2)

# View available rooms
available_rooms = hotel.get_available_rooms()
for room in available_rooms:
        print(room)

# Customer makes a reservation
customer1.make_reservation(room1, "2025-05-01", "2025-05-05")

# View Alice's reservations
customer1.view_reservations()

# Customer cancels a reservation
customer1.cancel_reservation("RES001")

# View all rooms in the hotel
hotel.view_all_rooms()

# View all reservations of a customer
hotel.view_customer_reservations("CUST001")
```

---

## 4. Expected Output

```yaml
Room Number: 101, Type: Single, Price per Night: $100, Availability: True
Room Number: 102, Type: Double, Price per Night: $150, Availability: True
Room Number: 103, Type: Suite, Price per Night: $250, Availability: True

Reservation ID: RES001, Room: 101, Customer: Alice, Check-in: 2025-05-01, Check-out: 2025-05-05, Total Cost: $400.0

Room Number: 101, Type: Single, Price per Night: $100, Availability: True
Room Number: 102, Type: Double, Price per Night: $150, Availability: True
Room Number: 103, Type: Suite, Price per Night: $250, Availability: True

No reservation found with ID RES001.
```

---

## 5. Constraints
- The system should handle multiple customers and reservations for the same room.
- A room should only be reserved if it is available for the specified dates.
- Customers can only cancel their own reservations.
- Implement basic error handling, such as attempting to book a room that is already reserved or canceling a non-existent reservation.
