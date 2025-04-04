# Assignment 5: Bank Account Management System

## Objective
Design and implement a **Bank Account Management System** using Object-Oriented Programming (OOP) principles. The system should allow users (customers) to manage their bank accounts, perform transactions (deposit, withdrawal), check their balances, and generate bank statements. Additionally, implement features such as account types, transaction history, and account transfers between different accounts.

---

## Requirements

### 1. Class Definitions

#### 1.1 BankAccount Class

**Attributes:**
- `account_number` (string): A unique identifier for each account.
- `account_holder` (string): The name of the account holder.
- `balance` (float): The current balance of the account (initially set to 0).
- `account_type` (string): The type of account (e.g., 'Checking', 'Savings').
- `transaction_history` (list): A list to store transaction details (deposit/withdrawal with amount and timestamp).

**Methods:**
- **Constructor (`__init__`)**: Initializes the account with the given account number, holder's name, account type, and balance.
- **`deposit(amount)`**: Deposits the specified amount into the account and records the transaction.
- **`withdraw(amount)`**: Withdraws the specified amount from the account if sufficient funds are available, and records the transaction. If insufficient balance, prints an error message.
- **`get_balance()`**: Returns the current balance of the account.
- **`view_transaction_history()`**: Displays all the transactions that have been made to/from the account.
- **`__str__()`**: Returns a string representation of the account in the format:
    ```
    Account Holder: <account_holder>, Account Number: <account_number>, Type: <account_type>, Balance: $<balance>
    ```

#### 1.2 Customer Class

**Attributes:**
- `customer_name` (string): The name of the customer.
- `customer_id` (string): A unique identifier for each customer.
- `accounts` (list): A list to store the customer's bank accounts (could be checking and/or savings).

**Methods:**
- **Constructor (`__init__`)**: Initializes the customer with their name and ID.
- **`open_account(account_type)`**: Creates a new `BankAccount` of the specified type and adds it to the customer's list of accounts.
- **`close_account(account_number)`**: Closes the specified account by account number and removes it from the list of accounts.
- **`view_accounts()`**: Displays all the accounts associated with the customer.
- **`get_account(account_number)`**: Returns the account object for a given account number.

#### 1.3 Bank Class

**Attributes:**
- `bank_name` (string): The name of the bank.
- `customers` (list): A list of all customers of the bank.

**Methods:**
- **Constructor (`__init__`)**: Initializes the bank with its name and an empty list of customers.
- **`add_customer(customer)`**: Adds a new customer to the bank.
- **`remove_customer(customer_id)`**: Removes a customer from the bank by their customer ID.
- **`get_customer(customer_id)`**: Returns the customer object for a given customer ID.
- **`view_all_customers()`**: Lists all customers of the bank.

---

### 2. Features

#### 2.1 Transactions
- Implement deposit and withdrawal operations for `BankAccount`.
- Each transaction should be logged in the transaction history with the amount, date, and type (deposit/withdrawal).

#### 2.2 Account Types
- Allow different account types (e.g., Checking, Savings).
- Implement specific behaviors for each account type (e.g., restrictions on withdrawals for Savings accounts).

#### 2.3 Balance and Transfer
- Ensure that when a withdrawal is made, the balance is updated accordingly.
- Add a method to transfer money from one account to another. This method should handle both the source and destination accounts, ensuring that the source account has enough funds for the transfer.

#### 2.4 Statement Generation
- Provide a method in `BankAccount` to generate a monthly statement that lists the balance and all transactions (deposits, withdrawals) made during the month.

---

### 3. Input Validation and Error Handling
- Ensure proper validation for all operations:
    - Withdrawal should fail if there are insufficient funds.
    - Deposit should only allow positive amounts.
    - Account numbers should be unique and valid.
    - Ensure that no transactions can happen on closed accounts.

---

### 4. Example Usage

```python
# Create a bank instance
bank = Bank("XYZ Bank")

# Create customer objects
customer1 = Customer("Alice", "CUST001")
customer2 = Customer("Bob", "CUST002")

# Add customers to the bank
bank.add_customer(customer1)
bank.add_customer(customer2)

# Customer opens accounts
customer1.open_account("Checking")
customer1.open_account("Savings")

# Perform transactions on Alice's accounts
checking_account = customer1.get_account("CHK12345")
checking_account.deposit(1000)
checking_account.withdraw(200)

# Perform transactions on Bob's account
savings_account = customer2.open_account("Savings")
savings_account.deposit(500)
savings_account.withdraw(100)

# Display bank's customer list
bank.view_all_customers()

# Display Alice's account details and transaction history
customer1.view_accounts()
checking_account.view_transaction_history()

# Transfer funds from one account to another
checking_account.transfer(100, savings_account)
```

---

### 5. Expected Output

```yaml
Customer Name: Alice, ID: CUST001
Customer Name: Bob, ID: CUST002

Account Holder: Alice, Account Number: CHK12345, Type: Checking, Balance: $800.0
Transaction History: [('Deposit', 1000), ('Withdrawal', 200)]

Account Holder: Bob, Account Number: SAV67890, Type: Savings, Balance: $400.0
Transaction History: [('Deposit', 500), ('Withdrawal', 100)]

Transfer Successful: $100 from Checking (Alice) to Savings (Bob)
```

---

### Constraints
- The `BankAccount` class must handle basic account operations such as deposit, withdrawal, and balance inquiry.
- Each account should have a unique account number.
- The system should handle basic error cases like insufficient funds for withdrawals or invalid account numbers.
- The `Bank` class should maintain a list of customers and their associated bank accounts.
