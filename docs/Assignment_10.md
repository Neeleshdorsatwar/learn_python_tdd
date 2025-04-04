### Problem Statement: Fitness Tracker System for Tracking Workouts and Health Metrics

#### Objective:
Design and implement a **Fitness Tracker System** using Object-Oriented Programming (OOP) principles. The system will allow users to track their workouts, monitor health metrics, and visualize their progress. The tracker will include functionality for logging different types of exercises, tracking calories burned, monitoring heart rate, step counts, sleep, and other health-related metrics over time. Users should be able to view their daily, weekly, and monthly progress reports.

#### Requirements:

### 1. **Class Definitions**

#### 1.1 **User Class**
- **Attributes:**
    - `user_id` (string): A unique identifier for the user (e.g., "USER001").
    - `name` (string): The name of the user.
    - `age` (int): The age of the user.
    - `gender` (string): The gender of the user (e.g., "Male", "Female").
    - `weight` (float): The weight of the user in kilograms.
    - `height` (float): The height of the user in centimeters.
    - `workouts` (list): A list of all workouts logged by the user. Each workout is represented by a `Workout` object.
    - `health_metrics` (list): A list of health metrics, such as heart rate, step count, calories burned, etc., logged over time.

- **Methods:**
    - **Constructor (`__init__`)**: Initializes the user with their `user_id`, `name`, `age`, `gender`, `weight`, `height`, and empty lists for `workouts` and `health_metrics`.
    - **`log_workout(workout)`**: Logs a new workout, adding it to the user's list of workouts.
    - **`log_health_metric(metric)`**: Logs a new health metric, adding it to the user's health metrics.
    - **`view_progress()`**: Displays the user's progress, including total workouts, calories burned, and health metrics.
    - **`__str__()`**: Returns a string representation of the user, including their basic information (name, age, weight, height).

#### 1.2 **Workout Class**
- **Attributes:**
    - `workout_id` (string): A unique identifier for the workout (e.g., "WORKOUT001").
    - `exercise_type` (string): The type of exercise performed (e.g., "Running", "Cycling", "Yoga").
    - `duration` (float): The duration of the workout in minutes.
    - `calories_burned` (float): The number of calories burned during the workout.
    - `date` (string): The date the workout was completed (e.g., "2025-04-01").
    - `heart_rate` (float): The average heart rate during the workout.

- **Methods:**
    - **Constructor (`__init__`)**: Initializes the workout with the `workout_id`, `exercise_type`, `duration`, `calories_burned`, `date`, and `heart_rate`.
    - **`__str__()`**: Returns a string representation of the workout, including its type, duration, calories burned, and heart rate.

#### 1.3 **HealthMetric Class**
- **Attributes:**
    - `metric_id` (string): A unique identifier for the health metric (e.g., "METRIC001").
    - `metric_type` (string): The type of health metric being recorded (e.g., "Step Count", "Heart Rate", "Sleep").
    - `value` (float): The value of the metric (e.g., number of steps, average heart rate).
    - `date` (string): The date the health metric was recorded (e.g., "2025-04-01").

- **Methods:**
    - **Constructor (`__init__`)**: Initializes the health metric with the `metric_id`, `metric_type`, `value`, and `date`.
    - **`__str__()`**: Returns a string representation of the health metric, including the metric type, value, and date.

#### 1.4 **FitnessTracker Class**
- **Attributes:**
    - `users` (list): A list of all users of the fitness tracker system.

- **Methods:**
    - **Constructor (`__init__`)**: Initializes the fitness tracker with an empty list of users.
    - **`add_user(user)`**: Adds a new user to the tracker system.
    - **`get_user_by_id(user_id)`**: Returns a user object based on their unique `user_id`.
    - **`view_user_progress(user_id)`**: Displays the progress of a specific user, including their logged workouts, health metrics, and other relevant data.
    - **`view_all_users()`**: Displays a list of all users registered in the system.

### 2. **Features**

#### 2.1 **Workout Logging**
- Users should be able to log different types of workouts, including the exercise type, duration, calories burned, and average heart rate.
- Each workout should be stored with a unique ID and associated with a specific date.

#### 2.2 **Health Metric Tracking**
- The system should allow users to track various health metrics, such as:
    - **Step Count**: Total steps taken during a given day.
    - **Heart Rate**: Average heart rate during the workout or at specific intervals.
    - **Calories Burned**: The number of calories burned during the workout.
    - **Sleep Data**: Total hours slept, or quality of sleep tracked by the user.

#### 2.3 **Progress Tracking**
- Users can view their progress over time, including:
    - The total number of workouts completed.
    - Total calories burned over a period (daily, weekly, monthly).
    - Average heart rate during workouts.
    - Step count trends, sleep patterns, or other health metrics tracked over time.

#### 2.4 **User and Workout Management**
- The system should allow for multiple users to be added, each with their own set of workouts and health metrics.
- Workouts and health metrics can be added by the user or automatically logged by the fitness tracker app or device.
    
#### 2.5 **Progress Reports**
- Users can view detailed reports on their fitness progress, including summaries of workouts, health metrics, and trends over different periods (daily, weekly, monthly).

### 3. **Sample Usage**

```python
# Create a fitness tracker instance
tracker = FitnessTracker()

# Create a new user
user1 = User("USER001", "Alice", 30, "Female", 65.5, 165)
tracker.add_user(user1)

# Log some workouts for the user
workout1 = Workout("WORKOUT001", "Running", 30, 300, "2025-04-01", 140)
workout2 = Workout("WORKOUT002", "Cycling", 45, 400, "2025-04-02", 130)
user1.log_workout(workout1)
user1.log_workout(workout2)

# Log health metrics
metric1 = HealthMetric("METRIC001", "Step Count", 8000, "2025-04-01")
metric2 = HealthMetric("METRIC002", "Heart Rate", 135, "2025-04-02")
user1.log_health_metric(metric1)
user1.log_health_metric(metric2)

# View user's progress
user1.view_progress()

# View detailed information of a specific workout
print(workout1)

# View all users in the fitness tracker system
tracker.view_all_users()

# View a specific user's progress
tracker.view_user_progress("USER001")
```

### 4. **Expected Output**

```
User: Alice, Age: 30, Weight: 65.5kg, Height: 165cm

Workout ID: WORKOUT001, Exercise: Running, Duration: 30 minutes, Calories Burned: 300, Heart Rate: 140 bpm
Workout ID: WORKOUT002, Exercise: Cycling, Duration: 45 minutes, Calories Burned: 400, Heart Rate: 130 bpm

Health Metric: Step Count, Value: 8000, Date: 2025-04-01
Health Metric: Heart Rate, Value: 135, Date: 2025-04-02

Progress Summary:
Total Workouts: 2
Total Calories Burned: 700
Average Heart Rate: 135 bpm
Step Count: 8000 steps (2025-04-01)

All users in the system:
1. Alice (USER001)

Progress of Alice:
- Total Workouts: 2
- Total Calories Burned: 700
- Average Heart Rate: 135 bpm
```

### 5. **Constraints:**
- The system should handle multiple users with independent workout and health tracking data.
- Health metrics such as heart rate, step count, and calories should be updated regularly.
- Workouts can vary in type and duration, and the system should handle all types of activities efficiently.
- Reports should provide users with insights into their fitness and health trends over time.

---

This **Fitness Tracker System** provides a comprehensive solution for users to track their workouts, monitor health metrics, and visualize their fitness progress. It helps users stay motivated and make data-driven decisions about their health and exercise routines.