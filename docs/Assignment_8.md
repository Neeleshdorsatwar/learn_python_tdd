# Problem Statement: Movie Ticket Booking System

## Objective
Design and implement a Movie Ticket Booking System using Object-Oriented Programming (OOP) principles. The system will allow users (customers) to view available movies, book tickets, view booking details, and cancel bookings. Movie theaters should be able to manage movies, schedules, and available seats. Additionally, the system should support different types of customers, such as regular and VIP, with varying seat prices.

---

## Requirements

### 1. Class Definitions

#### 1.1 Movie Class
**Attributes:**
- `movie_id` (string): A unique identifier for each movie (e.g., "MOV001").
- `title` (string): The title of the movie.
- `genre` (string): The genre of the movie (e.g., "Action", "Comedy").
- `duration` (int): The duration of the movie in minutes.
- `showtimes` (list): A list of available showtimes for the movie. Each showtime is represented by a `Showtime` object.

**Methods:**
- `__init__`: Initializes the movie with the `movie_id`, `title`, `genre`, `duration`, and an empty list of `showtimes`.
- `add_showtime(showtime)`: Adds a `Showtime` object to the movie's list of showtimes.
- `view_showtimes()`: Displays the available showtimes for the movie.

#### 1.2 Showtime Class
**Attributes:**
- `showtime_id` (string): A unique identifier for the showtime (e.g., "ST001").
- `date` (string): The date of the showtime (e.g., "2025-05-01").
- `time` (string): The time of the showtime (e.g., "7:00 PM").
- `seats_available` (int): The number of available seats for the showtime.
- `seat_price` (float): The price of a regular ticket for the showtime.

**Methods:**
- `__init__`: Initializes the showtime with the `showtime_id`, `date`, `time`, `seats_available`, and `seat_price`.
- `book_ticket(seat_count)`: Books the specified number of seats for the showtime and reduces the number of available seats.
- `cancel_booking(seat_count)`: Cancels a specified number of bookings and increases the available seats.
- `__str__`: Returns a string representation of the showtime in the format:
    ```
    Showtime ID: <showtime_id>, Movie: <movie_title>, Date: <date>, Time: <time>, Seats Available: <seats_available>, Ticket Price: $<seat_price>
    ```

#### 1.3 Customer Class
**Attributes:**
- `customer_id` (string): A unique identifier for the customer (e.g., "CUST001").
- `customer_name` (string): The name of the customer.
- `ticket_bookings` (list): A list of tickets booked by the customer. Each booking is an instance of the `TicketBooking` class.
- `customer_type` (string): The type of customer, such as "Regular" or "VIP". VIP customers may have special discounts or seat preferences.

**Methods:**
- `__init__`: Initializes the customer with their `customer_id`, `customer_name`, and `customer_type`.
- `book_ticket(showtime, seat_count)`: Books a specified number of seats for a given showtime.
- `cancel_booking(booking_id)`: Cancels an existing booking by its booking ID.
- `view_bookings()`: Displays a list of the customer's ticket bookings, showing movie titles, showtimes, and seat counts.

#### 1.4 TicketBooking Class
**Attributes:**
- `booking_id` (string): A unique identifier for the booking.
- `showtime` (`Showtime`): The showtime for which the ticket was booked.
- `customer` (`Customer`): The customer who made the booking.
- `seat_count` (int): The number of seats booked for the showtime.
- `total_cost` (float): The total cost of the booking, which depends on the number of seats and the seat price.

**Methods:**
- `__init__`: Initializes the booking with the `booking_id`, `showtime`, `customer`, `seat_count`, and calculates the `total_cost`.
- `calculate_total_cost()`: Calculates the total cost of the booking based on the number of seats and the seat price (including any discount for VIP customers).
- `__str__`: Returns a string representation of the ticket booking in the format:
    ```
    Booking ID: <booking_id>, Movie: <movie_title>, Showtime: <showtime_date> <showtime_time>, Seats: <seat_count>, Total Cost: $<total_cost>
    ```

#### 1.5 Cinema Class
**Attributes:**
- `cinema_name` (string): The name of the cinema.
- `movies` (list): A list of all movies being shown in the cinema.

**Methods:**
- `__init__`: Initializes the cinema with its `cinema_name` and an empty list of movies.
- `add_movie(movie)`: Adds a new `Movie` object to the cinema's list of movies.
- `view_movies()`: Displays a list of all movies available at the cinema, including their genres and durations.
- `view_movie_showtimes(movie_id)`: Displays a list of available showtimes for a specific movie.
- `get_movie_by_id(movie_id)`: Returns the `Movie` object for a given movie ID.

---

## Features

### 2.1 Movie Management
- The system should allow the cinema to manage a list of movies, each with its own showtimes.
- Each movie will have one or more showtimes with different dates, times, and availability.

### 2.2 Ticket Booking
- Customers should be able to view the available movies and their showtimes.
- Customers can book tickets for a given showtime if seats are available.
- The number of available seats for each showtime should be updated when tickets are booked.
- VIP customers should receive a discount on ticket prices (e.g., 10% off).

### 2.3 Booking Cancellation
- Customers should be able to cancel a booking and release the reserved seats for others.
- When a booking is canceled, the number of available seats for that showtime should be updated accordingly.

### 2.4 Customer View
- Customers should be able to view all their bookings, including movie titles, showtimes, and total cost.
- Customers can cancel bookings if needed.

---

## Sample Usage

```python
# Create a cinema instance
cinema = Cinema("Grand Cinemas")

# Create some movies and add them to the cinema
movie1 = Movie("MOV001", "The Avengers", "Action", 120)
movie2 = Movie("MOV002", "The Incredibles", "Animation", 90)

cinema.add_movie(movie1)
cinema.add_movie(movie2)

# Create showtimes for the movies
showtime1 = Showtime("ST001", "2025-05-01", "7:00 PM", 100, 12.99)
showtime2 = Showtime("ST002", "2025-05-01", "9:00 PM", 50, 14.99)

movie1.add_showtime(showtime1)
movie1.add_showtime(showtime2)

# Create customers
customer1 = Customer("Alice", "CUST001", "Regular")
customer2 = Customer("Bob", "CUST002", "VIP")

# Book tickets
customer1.book_ticket(showtime1, 2)
customer2.book_ticket(showtime1, 3)

# View bookings
customer1.view_bookings()
customer2.view_bookings()

# Cancel booking
customer1.cancel_booking("B001")

# View available showtimes for a movie
cinema.view_movie_showtimes("MOV001")
```

---

## Expected Output

```yaml
Movie Title: The Avengers, Genre: Action, Duration: 120 minutes
Showtime ID: ST001, Movie: The Avengers, Date: 2025-05-01, Time: 7:00 PM, Seats Available: 100, Ticket Price: $12.99
Showtime ID: ST002, Movie: The Avengers, Date: 2025-05-01, Time: 9:00 PM, Seats Available: 50, Ticket Price: $14.99

Booking ID: B001, Movie: The Avengers, Showtime: 2025-05-01 7:00 PM, Seats: 2, Total Cost: $25.98
Booking ID: B002, Movie: The Avengers, Showtime: 2025-05-01 7:00 PM, Seats: 3, Total Cost: $40.48

Booking ID: B001, Movie: The Avengers, Showtime: 2025-05-01 7:00 PM, Seats: 2, Total Cost: $25.98

Available Showtimes for The Avengers:
Showtime ID: ST001, Movie: The Avengers, Date: 2025-05-01, Time: 7:00 PM, Seats Available: 100, Ticket Price: $12.99
Showtime ID: ST002, Movie: The Avengers, Date: 2025-05-01, Time: 9:00 PM, Seats Available: 50, Ticket Price: $14.99
```

---

## Constraints
- The system should handle multiple customers booking tickets for the same showtime.
- The system should update seat availability after each booking or cancellation.
- VIP customers should receive a discount on ticket prices.
- Implement basic error handling, such as attempting to book more seats than available or canceling a non-existent booking.
