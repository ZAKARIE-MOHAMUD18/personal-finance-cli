# Personal Finance Tracker CLI

A simple command-line application to manage personal finances. This tool allows users to create accounts, record transactions, categorize them, view balances, and generate basic reports. It is built using **Python**, **SQLAlchemy**, and **Alembic** for database migrations.

---

## CLI Script (`cli.py`)

The `cli.py` script is the main interface for interacting with the Personal Finance Tracker. It provides a text-based menu to perform all user actions:

- **Create Account**: Add a new account with a name and initial balance.
- **List Accounts**: View all accounts with their current balances.
- **Add Category**: Create a new transaction category, such as Food, Bills, or Salary.
- **List Categories**: View all categories in the system.
- **Add Transaction**: Record a transaction by selecting an account and category, entering a description, and specifying an amount (positive for income, negative for expense). The account balance updates automatically.
- **List Transactions**: Display all transactions with details including account, category, amount, and date.
- **Update Transaction**: Modify an existing transaction in case of mistakes.
- **Delete Transaction**: Remove a transaction from the database.
- **Report by Category**: Summarize transactions grouped by category to analyze spending habits.
- **Report by Date**: Show transactions for a specific date.

The CLI ensures users can fully manage their finances from the terminal in a straightforward manner.

---

## Functions Overview

- `create_account(session)`: Prompts the user for an account name and initial balance, creates the account, and saves it to the database.
- `list_accounts(session)`: Retrieves and prints all accounts with balances in a table format.
- `add_category(session)`: Adds a new category for transactions.
- `list_categories(session)`: Displays all categories.
- `add_transaction(session)`: Lets the user record a transaction with description, amount, account, and category.
- `list_transactions(session)`: Shows all transactions in a readable table.
- `update_transaction(session)`: Updates the description or amount of a transaction.
- `delete_transaction(session)`: Deletes a selected transaction.
- `report_by_category(session)`: Generates a summary of totals for each category.
- `report_by_date(session)`: Lists transactions filtered by a specific date.

---

## Models (`models.py`)

The project uses **SQLAlchemy ORM** to manage the database tables:

- **Account**: Represents a financial account (e.g., checking, savings) with a name and balance. It has a relationship to transactions.
- **Category**: Represents a category of spending or income (e.g., Food, Bills, Salary). Linked to transactions.
- **Transaction**: Represents a single transaction, including description, amount, timestamp, linked account, and category.

---

## Database (`db.py`)

This file sets up the database connection and session handling:

- `engine` and `SessionLocal`: Create a connection to the SQLite database (`personal_finance.db`) and manage sessions.
- `Base`: The declarative base for all models.
- `db.db()`: Initializes the database tables based on the models.

Alembic handles migrations for this database, allowing schema updates without losing data.

---

## Optional Seed Script (`seed_db.py`)

A simple script to populate the database with initial accounts and categories:

- Creates default accounts like "Checking" and "Savings".
- Adds categories such as "Food", "Bills", and "Salary".
- Useful for testing the CLI without manually adding accounts and categories first.

---

## Dependencies

The project relies on:

- **Python 3.8.13**  
- **SQLAlchemy** – ORM for managing database models  
- **Alembic** – For database migrations  
- **Tabulate** – For nicely formatted tables in the terminal  

All dependencies are managed via **Pipenv** (`Pipfile` and `Pipfile.lock`).

---

## Usage
```
1.install pipenv:-
   ( pipenv install )

2.Activate your environment:-
   ( pipenv shell )

2. install the dependencies:-
    ( pipenv install sqlalchemy alembic tabulate )

3. Launch the CLI:-
    ( python cli.py )

## Example CLI Session
```
--- Personal Finance Tracker ---

1.Create account

2.List accounts

3.Add category

4.List categories

5.Add transaction

6.List transactions

7.Update transaction

8.Delete transaction

9.Report by category

10.Report by date

0.Exit

Choose: 1

Enter account name: Checking
Enter initial balance: 1000
Account "Checking" created successfully.

Choose: 3
Enter category name: Food
Category "Food" added successfully.

Choose: 5
Select account ID: 1
Select category ID: 1
Enter description: Lunch
Enter amount: -300
Transaction added successfully.

Choose: 2
Accounts:
ID Name Balance
1 Checking 700 



## Resources

- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [Tabulate Documentation](https://pypi.org/project/tabulate/)
