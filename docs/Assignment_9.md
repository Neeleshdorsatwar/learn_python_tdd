# Problem Statement: Employee Management System (Records, Payroll, and Leave Requests)

## Objective
Design and implement an Employee Management System using Object-Oriented Programming (OOP) principles. This system will allow a company to manage employee records, calculate payroll, and handle leave requests. The system should track employee details such as personal information, roles, salary, and leave history. It should also handle the processing of leave requests, including approval/rejection and updating leave balances.

---

## Requirements

### 1. Class Definitions

#### 1.1 Employee Class

**Attributes:**
- `employee_id` (string): A unique identifier for each employee (e.g., "EMP001").
- `first_name` (string): The first name of the employee.
- `last_name` (string): The last name of the employee.
- `email` (string): The email address of the employee.
- `position` (string): The job title or position of the employee (e.g., "Software Developer", "Manager").
- `salary` (float): The base salary of the employee.
- `leave_balance` (int): The number of leave days available for the employee.

**Methods:**
- `__init__`: Initializes the employee with the given `employee_id`, `first_name`, `last_name`, `email`, `position`, `salary`, and `leave_balance`.
- `update_salary(new_salary)`: Updates the salary of the employee.
- `update_leave_balance(days)`: Updates the leave balance by adding or subtracting the specified number of days.
- `__str__()`: Returns a string representation of the employee, including their full name, position, salary, and leave balance.

---

#### 1.2 LeaveRequest Class

**Attributes:**
- `request_id` (string): A unique identifier for each leave request (e.g., "LR001").
- `employee` (Employee): The employee who is requesting the leave.
- `start_date` (string): The start date of the leave (e.g., "2025-05-01").
- `end_date` (string): The end date of the leave (e.g., "2025-05-05").
- `leave_days` (int): The number of leave days requested.
- `status` (string): The status of the leave request (e.g., "Pending", "Approved", "Rejected").

**Methods:**
- `__init__`: Initializes the leave request with the `request_id`, `employee`, `start_date`, `end_date`, and `status`.
- `calculate_leave_days()`: Calculates the total number of leave days requested based on the start and end date.
- `approve_request()`: Approves the leave request and updates the status to "Approved".
- `reject_request()`: Rejects the leave request and updates the status to "Rejected".
- `__str__()`: Returns a string representation of the leave request in the format:
    ```
    Leave Request ID: <request_id>, Employee: <employee_name>, Dates: <start_date> to <end_date>, Status: <status>
    ```

---

#### 1.3 Payroll Class

**Attributes:**
- `payroll_id` (string): A unique identifier for each payroll entry (e.g., "PAY001").
- `employee` (Employee): The employee for whom the payroll is being processed.
- `total_pay` (float): The total pay to be issued to the employee (including deductions, bonuses, etc.).
- `bonus` (float): The bonus amount added to the employee’s pay.
- `deductions` (float): The deductions made from the employee's pay (e.g., taxes, insurance).

**Methods:**
- `__init__`: Initializes the payroll with the `payroll_id`, `employee`, `total_pay`, `bonus`, and `deductions`.
- `calculate_total_pay()`: Calculates the total pay by adding the bonus and subtracting the deductions from the employee's salary.
- `__str__()`: Returns a string representation of the payroll in the format:
    ```
    Payroll ID: <payroll_id>, Employee: <employee_name>, Total Pay: $<total_pay>, Bonus: $<bonus>, Deductions: $<deductions>
    ```

---

#### 1.4 EmployeeManager Class

**Attributes:**
- `employees` (list): A list of all employees in the company.
- `leave_requests` (list): A list of all leave requests made by employees.
- `payrolls` (list): A list of payroll records for employees.

**Methods:**
- `__init__`: Initializes the employee manager with empty lists for employees, leave requests, and payrolls.
- `add_employee(employee)`: Adds a new employee to the employee list.
- `get_employee_by_id(employee_id)`: Returns an employee object by their unique `employee_id`.
- `view_all_employees()`: Displays a list of all employees and their basic details.
- `request_leave(employee, start_date, end_date)`: Allows an employee to request leave by providing the start and end date.
- `approve_leave_request(request_id)`: Approves a leave request by its unique `request_id`.
- `reject_leave_request(request_id)`: Rejects a leave request by its unique `request_id`.
- `process_payroll(employee_id)`: Processes the payroll for an employee, calculating their total pay.
- `view_employee_payroll(employee_id)`: Displays the payroll details of a specific employee.

---

## 2. Features

### 2.1 Employee Management
- The system should allow for the addition and removal of employees, including updating their personal and employment information.
- Employees should have a salary, a leave balance, and the ability to update this information when needed.

### 2.2 Leave Requests
- Employees can submit leave requests, specifying the start and end dates.
- Leave requests are initially set to "Pending" and need to be approved or rejected by the system.
- Once approved, the employee’s leave balance should be updated accordingly.

### 2.3 Payroll Processing
- The system should calculate and generate payroll for each employee based on their salary, bonuses, and deductions (e.g., taxes, insurance).
- Payroll should be generated periodically (e.g., monthly).
- The total pay should be calculated by adding bonuses and subtracting deductions from the base salary.

### 2.4 Reports and Viewing Information
- Employees should be able to view their personal information, leave balance, and payroll details.
- Managers can view all employee records, leave requests, and payrolls.

---

## 3. Sample Usage

```python
# Create an employee manager instance
manager = EmployeeManager()

# Add some employees
emp1 = Employee("EMP001", "Alice", "Smith", "alice@example.com", "Software Developer", 5000, 15)
emp2 = Employee("EMP002", "Bob", "Johnson", "bob@example.com", "Manager", 6000, 20)

manager.add_employee(emp1)
manager.add_employee(emp2)

# View all employees
manager.view_all_employees()

# Request leave for an employee
leave_request1 = manager.request_leave(emp1, "2025-05-01", "2025-05-05")

# Approve leave request
manager.approve_leave_request(leave_request1.request_id)

# Process payroll for an employee
payroll1 = manager.process_payroll("EMP001")

# View payroll details for an employee
manager.view_employee_payroll("EMP001")
```

---

## 4. Expected Output

```yaml
Employee ID: EMP001, Name: Alice Smith, Position: Software Developer, Salary: $5000, Leave Balance: 15
Employee ID: EMP002, Name: Bob Johnson, Position: Manager, Salary: $6000, Leave Balance: 20

Leave Request ID: LR001, Employee: Alice Smith, Dates: 2025-05-01 to 2025-05-05, Status: Approved

Payroll ID: PAY001, Employee: Alice Smith, Total Pay: $5200, Bonus: $200, Deductions: $0
```

---

## 5. Constraints
- Employees should only be able to request leave if they have enough leave days available.
- Leave requests should not overlap with other approved leave requests.
- Payroll should be processed at regular intervals, and deductions should be automatically calculated.
