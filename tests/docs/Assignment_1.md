# Assignment 1

#### Objective

Your task is to design and implement a `Calculator` class in Python that simulates a basic calculator's functionality. The calculator should be able to perform arithmetic operations such as addition, subtraction, multiplication, and division.

---

#### Requirements

**Class Definition**  
- Define a class named `Calculator`.
- The class should contain the following operations:
    - **Addition (`add`)**: Takes two numbers and returns their sum.
    - **Subtraction (`subtract`)**: Takes two numbers and returns their difference.
    - **Multiplication (`multiply`)**: Takes two numbers and returns their product.
    - **Division (`divide`)**: Takes two numbers and returns their quotient. Handle division by zero by raising a `ZeroDivisionError` or returning a suitable error message.

**Constructor**  
- The `Calculator` class should have a constructor to initialize an attribute called `result` to store the result of the last calculation.

**Method to Clear Results**  
- Implement a method `clear()` that resets the `result` attribute to `0`.

**Method to Display Results**  
- Implement a method `get_result()` that returns the current result stored in the `result` attribute.

**Advanced Operation (Optional)**  
- **Exponentiation (`power`)**: Implement a method that calculates the result of raising a number to a power (e.g., `a^b`).

**Input Validation**  
- Ensure that the methods accept only valid numerical inputs. Raise appropriate exceptions or error messages for invalid inputs (e.g., strings or `None`).

**User Interaction (Optional for Extended Challenge)**  
- Provide a simple interface where the user can input operations and numbers (via function calls or prompts), and the calculator performs the calculations and displays the result.

---

#### Example

```python
# Example usage:

calc = Calculator()

calc.add(5, 3)      # Result should be 8
print(calc.get_result())  # Output: 8

calc.subtract(10, 4)   # Result should be 6
print(calc.get_result())  # Output: 6

calc.multiply(2, 3)   # Result should be 6
print(calc.get_result())  # Output: 6

calc.divide(10, 2)    # Result should be 5
print(calc.get_result())  # Output: 5

calc.divide(10, 0)    # Should raise ZeroDivisionError or return an error message

calc.clear()          # Resets the result to 0
print(calc.get_result())  # Output: 0
```

---

#### Constraints

- Ensure that your methods return appropriate results and handle edge cases like division by zero or invalid inputs.
- If the user calls multiple operations sequentially, the result should be updated accordingly.
