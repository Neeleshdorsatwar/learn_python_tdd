# Assignment 6: Student Grade and Assignment Management System

# Objective

Your task is to design and implement a **Student Grade and Assignment Management System** using Object-Oriented Programming (OOP) principles. This system will manage students' grades, assignments, and coursework for a specific class. The system should allow instructors to add assignments, grade students, and generate reports, while allowing students to view their grades and assignments.

---

## Requirements

### 1. Class Definitions

#### 1.1 Student Class

**Attributes:**
- `student_id` (string): A unique identifier for each student (e.g., student number).
- `student_name` (string): The name of the student.
- `assignments` (list): A list of assignments associated with the student. Each assignment is represented by an `Assignment` object.
- `grades` (dict): A dictionary where the key is the assignment name and the value is the grade/score for that assignment.

**Methods:**
- **Constructor (`__init__`)**: Initializes the student with their `student_id` and `student_name`.
- **`add_assignment(assignment)`**: Adds an `Assignment` object to the student's list of assignments.
- **`submit_assignment(assignment_name, score)`**: Submits a grade for a specific assignment.
- **`view_grades()`**: Returns a list of the student's grades, showing each assignment and the corresponding score.
- **`get_gpa()`**: Calculates and returns the student's GPA based on the grades for each assignment.
- **`__str__()`**: Returns a string representation of the student in the format:
    ```
    Student Name: <student_name>, ID: <student_id>, GPA: <GPA>
    ```

#### 1.2 Assignment Class

**Attributes:**
- `assignment_name` (string): The name of the assignment (e.g., "Midterm Exam").
- `due_date` (string): The due date for the assignment (e.g., "2025-05-15").
- `total_points` (float): The total number of points the assignment is worth.

**Methods:**
- **Constructor (`__init__`)**: Initializes the assignment with its `assignment_name`, `due_date`, and `total_points`.
- **`__str__()`**: Returns a string representation of the assignment in the format:
    ```
    Assignment Name: <assignment_name>, Due Date: <due_date>, Total Points: <total_points>
    ```

#### 1.3 Instructor Class

**Attributes:**
- `instructor_name` (string): The name of the instructor.
- `course_name` (string): The name of the course.
- `students` (list): A list of `Student` objects enrolled in the course.
- `assignments` (list): A list of `Assignment` objects that the instructor creates for the course.

**Methods:**
- **Constructor (`__init__`)**: Initializes the instructor with their `instructor_name`, `course_name`, and empty lists for students and assignments.
- **`add_student(student)`**: Adds a `Student` object to the list of enrolled students.
- **`create_assignment(assignment_name, due_date, total_points)`**: Creates a new `Assignment` object and adds it to the list of assignments for the course.
- **`assign_grades(student_id, assignment_name, grade)`**: Assigns a grade to a student for a specific assignment.
- **`view_class_report()`**: Displays a report of the class's performance, showing the GPA of all students and their assignments.

---

## 2. Features

### 2.1 Assignment Management
- The instructor should be able to create assignments with specific names, due dates, and total points.
- Students should be able to view the list of assignments for their course.

### 2.2 Grade Management
- The instructor should assign grades for each assignment to students.
- Students should be able to view their grades for each assignment.
- GPA calculation for each student should be based on the grades for all assignments.

### 2.3 Student Reports
- The system should allow students to view a list of all their assignments and corresponding grades.
- The GPA for each student should be displayed, calculated based on the weighted scores of all assignments.

### 2.4 Class Report
- The instructor should be able to generate a class report, which lists all students and their GPAs.

---

## 3. Sample Usage

```python
# Create an instructor and students
instructor = Instructor("Prof. John", "Computer Science 101")

student1 = Student("S12345", "Alice")
student2 = Student("S67890", "Bob")

# Add students to the course
instructor.add_student(student1)
instructor.add_student(student2)

# Create assignments for the course
assignment1 = Assignment("Midterm Exam", "2025-05-15", 100)
assignment2 = Assignment("Final Project", "2025-06-01", 150)

# Instructor assigns assignments to students
instructor.create_assignment("Midterm Exam", "2025-05-15", 100)
instructor.create_assignment("Final Project", "2025-06-01", 150)

# Students submit their grades for the assignments
student1.submit_assignment("Midterm Exam", 85)
student1.submit_assignment("Final Project", 120)

student2.submit_assignment("Midterm Exam", 90)
student2.submit_assignment("Final Project", 135)

# Instructor assigns grades to the assignments
instructor.assign_grades("S12345", "Midterm Exam", 85)
instructor.assign_grades("S12345", "Final Project", 120)

instructor.assign_grades("S67890", "Midterm Exam", 90)
instructor.assign_grades("S67890", "Final Project", 135)

# View student grades and GPA
print(student1.view_grades())
print(f"GPA: {student1.get_gpa()}")

print(student2.view_grades())
print(f"GPA: {student2.get_gpa()}")

# Instructor views class report
instructor.view_class_report()
```

---

## 4. Expected Output

```yaml
Student Name: Alice, ID: S12345
Assignment Name: Midterm Exam, Grade: 85
Assignment Name: Final Project, Grade: 120
GPA: 3.4

Student Name: Bob, ID: S67890
Assignment Name: Midterm Exam, Grade: 90
Assignment Name: Final Project, Grade: 135
GPA: 3.8

Class Report:
Alice: GPA = 3.4
Bob: GPA = 3.8
```

---

## 5. Constraints
- The GPA should be calculated based on the assignment scores and their total points. For example, the GPA could be a weighted average of all assignment scores.
- The system should handle invalid grades (e.g., negative scores, scores exceeding the total points).
- The instructor should be able to manage a list of assignments, assign grades, and generate class performance reports.
