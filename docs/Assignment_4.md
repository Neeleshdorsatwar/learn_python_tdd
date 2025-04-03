# Objective

Your task is to design and implement a **Toll Plaza Management System** that simulates the operations of a toll collection system for vehicles passing through a toll plaza. The system should allow vehicles to pay tolls based on vehicle types, manage the toll collection process, and generate reports on the total toll collected over a period.

---

## Requirements

### Part 1: Vehicle Class

#### Vehicle Class:

Create a `Vehicle` class with the following attributes:

- **`vehicle_id`** (string): A unique identifier for each vehicle (e.g., license plate number).
- **`vehicle_type`** (string): The type of vehicle (e.g., car, truck, motorcycle, etc.).
- **`toll_amount`** (float): The toll amount to be paid based on the vehicle type (initially set to 0).

The class should have the following methods:

1. **Constructor**: Initializes the vehicle with its `vehicle_id` and `vehicle_type`.
2. **`calculate_toll()`**: Calculates the toll based on the vehicle type:
    - Car = $5
    - Truck = $10
    - Motorcycle = $2
    - *(You can extend this list with other vehicle types as needed).*
3. **`__str__()`**: Returns a string representation of the vehicle in the format:
    ```
    Vehicle ID: <vehicle_id>, Type: <vehicle_type>, Toll: $<toll_amount>
    ```

---

### Part 2: Toll Plaza Class

#### TollPlaza Class:

Create a `TollPlaza` class that manages the toll collection process.

The class should have the following attributes:

- **`vehicles`** (list): A list to store all vehicles that pass through the toll plaza.
- **`total_collected_toll`** (float): The total toll amount collected by the toll plaza.

The class should have the following methods:

1. **`add_vehicle(vehicle)`**: Adds a `Vehicle` object to the toll plaza and calculates the toll for that vehicle.
2. **`process_payment(vehicle)`**: Processes the payment for the vehicle and adds the toll amount to `total_collected_toll`.
3. **`generate_report()`**: Returns a summary of the total toll collected, including the total number of vehicles processed and the total toll amount.
4. **`list_vehicles()`**: Returns a list of all vehicles that have passed through the toll plaza, displaying their `vehicle_id`, `vehicle_type`, and the toll they paid.

---

### Part 3: Additional Features

#### Vehicle Queue (Optional Feature):

- Implement a queue mechanism where vehicles are processed in the order they arrive at the toll plaza. You can use a queue to simulate this behavior (e.g., using a `list` or a `queue.Queue` in Python).

#### Discounts (Optional Feature):

- Implement a discount system for specific vehicles or vehicle types. For example, electric vehicles might receive a 50% discount on the toll.
- Add a method **`apply_discount(vehicle)`** that checks if the vehicle is eligible for a discount and reduces the toll amount accordingly.

#### Multiple Toll Lanes (Optional Feature):

- Simulate a system with multiple toll lanes. Vehicles can be assigned to different lanes, and each lane can collect tolls separately.
- The `TollPlaza` should have multiple lanes, and each lane should be capable of processing vehicles independently.

---

## Example Usage

```python
# Example usage:

# Create some vehicle objects
vehicle1 = Vehicle("ABC123", "car")
vehicle2 = Vehicle("XYZ789", "truck")
vehicle3 = Vehicle("LMN456", "motorcycle")

# Create a toll plaza
plaza = TollPlaza()

# Add vehicles to the toll plaza
plaza.add_vehicle(vehicle1)
plaza.add_vehicle(vehicle2)
plaza.add_vehicle(vehicle3)

# Process payments for vehicles
plaza.process_payment(vehicle1)
plaza.process_payment(vehicle2)
plaza.process_payment(vehicle3)

# Generate the report
plaza.generate_report()

# List all vehicles and tolls collected
plaza.list_vehicles()
```

### Expected Output:

```yaml
Vehicle ID: ABC123, Type: car, Toll: $5
Vehicle ID: XYZ789, Type: truck, Toll: $10
Vehicle ID: LMN456, Type: motorcycle, Toll: $2

Total Vehicles Processed: 3
Total Toll Collected: $17
```

---

## Constraints

1. The `TollPlaza` should not accept more than one payment for the same vehicle.
2. Ensure that vehicles of different types are charged according to the correct toll amount.
3. Optionally, handle discounts for eligible vehicles and track tolls for each lane (if implemented).
4. The system should maintain a record of all vehicles passing through the plaza and should be able to generate a report of the total toll collected at any point in time.

---

## Bonus (Optional)

1. Implement a method to refund toll payments if necessary (e.g., for faulty transactions).
2. Implement peak hours logic where toll rates might vary based on the time of day (e.g., a surcharge during rush hours).