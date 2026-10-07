# Student Expense Tracker — Project Documentation

## 1. Introduction

The Student Expense Tracker is a Python-based Command Line Interface (CLI) application developed to manage student expense records.

The application uses **Python** for the application logic and **SQLite** for persistent data storage.

Users can:

- Add new expenses
- View all expenses
- Search expenses
- Update existing expenses
- Delete expenses
- Exit the application

The project is organized into separate modules so that database operations, validation, and application control are handled independently.

---

# 2. Objectives

The main objectives of the project are:

1. To develop a simple CLI-based expense management application.
2. To implement complete CRUD operations.
3. To store expense data persistently using SQLite.
4. To validate user input before storing it.
5. To separate application logic into reusable Python modules.
6. To provide a simple and reliable interface for managing expenses.

---

# 3. System Architecture

The project follows a simple modular architecture.

```text
                    ┌─────────────────────┐
                    │      main.py        │
                    │  Application / CLI  │
                    └──────────┬──────────┘
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ▼                             ▼
       ┌─────────────────┐          ┌─────────────────┐
       │ validation.py   │          │    crud.py      │
       │ Input Validation│          │ CRUD Operations │
       └─────────────────┘          └────────┬────────┘
                                             │
                                             ▼
                                   ┌─────────────────┐
                                   │   database.py   │
                                   │ SQLite Connection│
                                   └────────┬────────┘
                                            │
                                            ▼
                                   ┌─────────────────┐
                                   │ expenses.db     │
                                   │ SQLite Database  │
                                   └─────────────────┘


Architecture Components
main.py

Acts as the main entry point of the application.

Responsibilities:

Display the CLI menu
Accept user choices
Collect user input
Call validation functions
Call CRUD functions
Control the main application loop
crud.py

Contains database-related operations for expenses.

Responsibilities:

Insert expenses
Retrieve expenses
Search expenses
Update expenses
Delete expenses
Check whether an expense exists
database.py

Handles SQLite database setup.

Responsibilities:

Define the database path
Create the database directory
Establish SQLite connections
Create the expenses table
validation.py

Contains functions used to validate user input.

Responsibilities:

Validate text fields
Validate expense amounts
Validate expense IDs
Validate dates
4. Project Structure
student-expense-tracker/
│
├── data/
│   └── .gitkeep
│
├── docs/
│   └── documentation.md
│
├── .gitignore
├── crud.py
├── database.py
├── main.py
├── README.md
├── requirements.txt
└── validation.py

The SQLite database file is generated automatically inside the data directory when the application runs.

5. Database Design

The application uses SQLite as its database.

The database file is:

data/expenses.db

The application creates the database and table automatically if they do not already exist.

Expenses Table

The database contains one table named:

expenses
Database Schema
Column	Data Type	Constraint	Description
id	INTEGER	PRIMARY KEY, AUTOINCREMENT	Unique expense identifier
description	TEXT	NOT NULL	Description of the expense
category	TEXT	NOT NULL	Expense category
amount	REAL	NOT NULL	Expense amount
date	TEXT	NOT NULL	Date of the expense

The SQL table definition is:

CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    date TEXT NOT NULL
);
6. Database Connection

The database.py module contains the get_connection() function.

It uses Python's built-in sqlite3 module to connect to the database.

The database path is defined as:

DATABASE_PATH = Path("data/expenses.db")

Before connecting, the application creates the data directory if necessary.

DATABASE_PATH.parent.mkdir(exist_ok=True)

The connection is then created using:

sqlite3.connect(DATABASE_PATH)

Database connections are closed after operations are completed.

7. CRUD Operations

CRUD stands for:

C — Create
R — Read
U — Update
D — Delete

The project implements all four operations.

7.1 Create — Add Expense

The add_expense() function in crud.py inserts a new expense into the database.

SQL operation:

INSERT INTO expenses
(description, category, amount, date)
VALUES (?, ?, ?, ?);

The application uses parameterized SQL queries.

Example:

cursor.execute("""
    INSERT INTO expenses (description, category, amount, date)
    VALUES (?, ?, ?, ?)
""", (description, category, amount, date))

Using placeholders helps keep user-provided values separate from the SQL statement.

After the record is inserted, the transaction is saved using:

connection.commit()
7.2 Read — View All Expenses

The get_all_expenses() function retrieves all stored expense records.

SQL operation:

SELECT id, description, category, amount, date
FROM expenses
ORDER BY id;

The returned records are displayed in a formatted table in the terminal.

Example output format:

======================================================================
                    ALL EXPENSES
======================================================================
ID   Description         Category       Amount      Date
----------------------------------------------------------------------
1    Bus Ticket          Travel         ₹50.00      2026-10-06
======================================================================

If no records exist, the application displays:

No expenses found.
7.3 Search Expense

The search_expenses() function searches expenses using the description or category.

SQL operation:

SELECT id, description, category, amount, date
FROM expenses
WHERE description LIKE ? OR category LIKE ?
ORDER BY id;

The % wildcard is used to allow partial matching.

For example, searching for:

Travel

can find records with categories or descriptions containing Travel.

7.4 Update Expense

The update_expense() function modifies an existing expense using its ID.

SQL operation:

UPDATE expenses
SET description = ?,
    category = ?,
    amount = ?,
    date = ?
WHERE id = ?;

Before updating, main.py checks whether the specified expense ID exists using:

expense_exists(expense_id)

If the ID does not exist, the user receives:

Expense not found.

After a successful update, the transaction is committed to the database.

7.5 Delete Expense

The delete_expense() function removes an expense using its ID.

SQL operation:

DELETE FROM expenses
WHERE id = ?;

If the specified ID does not exist, the application displays:

Expense not found.

After a successful deletion, the transaction is committed.

8. Input Validation

Input validation is handled separately in validation.py.

Separating validation from the main application makes the code easier to maintain and reuse.

8.1 Non-Empty Validation

The validate_non_empty() function checks whether a text value contains meaningful input.

It is used for fields such as:

Description
Category
Search term

Example:

def validate_non_empty(value, field_name):
    if not value.strip():
        print(f"{field_name} cannot be empty.")
        return False

    return True

An empty value is rejected.

8.2 Amount Validation

The validate_amount() function checks whether the entered amount is a valid positive number.

The input is converted to a floating-point number.

Example valid values:

50
125.50
1000

Invalid values include:

abc
-50
0

The amount must be greater than zero.

8.3 ID Validation

The validate_id() function ensures that the entered expense ID is a positive integer.

Valid example:

5

Invalid examples:

abc
-2
0
8.4 Date Validation

The validate_date() function checks whether the entered date follows:

YYYY-MM-DD

The Python datetime.strptime() function is used for validation.

Example:

2026-10-06

is a valid date format.

An incorrectly formatted or invalid date is rejected.

9. Exception Handling

Database operations are protected using try, except, and finally.

General structure:

connection = get_connection()

try:
    # Database operation

except Exception as e:
    print("Error:", e)

finally:
    connection.close()

This provides three important behaviors:

Database operations are attempted inside the try block.
Errors are handled in the except block.
The database connection is closed in the finally block.

This helps prevent database connections from remaining open after an operation.

10. Application Execution Flow

When the application starts, the execution follows these steps:

Start
  │
  ▼
main.py
  │
  ▼
create_table()
  │
  ▼
Display Main Menu
  │
  ▼
Get User Choice
  │
  ├───────────────┐
  │               │
  ▼               ▼
Add Expense    View Expenses
  │               │
  ▼               ▼
Validate       Retrieve Data
Input              │
  │               ▼
  ▼            Display Data
Store in DB
  │
  └──────────────────────┐
                         │
                         ▼
                    Return to Menu
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
           Search     Update      Delete
              │          │          │
              └──────────┼──────────┘
                         │
                         ▼
                    Return to Menu
                         │
                         ▼
                       Exit
11. Detailed Execution Process
Step 1 — Application Starts

The following code runs:

if __name__ == "__main__":
    main()

This calls the main() function.

Step 2 — Database Table Creation

At the beginning of main():

create_table()

is called.

If the database or table does not exist, SQLite creates them.

If they already exist, they are left unchanged.

Step 3 — Menu Display

The application enters:

while True:

and displays the available operations.

1. Add Expense
2. View All Expenses
3. Search Expense
4. Update Expense
5. Delete Expense
6. Exit
Step 4 — User Input

The user's menu selection is read using:

choice = input("Enter your choice: ").strip()

The corresponding operation is then selected using if and elif statements.

Step 5 — Validation

For operations requiring user input, the appropriate validation functions are called.

For example:

amount = validate_amount(amount_input)

If validation fails, the user is asked to enter the value again.

Step 6 — Database Operation

After successful validation, main.py calls the appropriate function from crud.py.

For example:

add_expense(description, category, amount, date)

The CRUD function performs the SQL operation on the SQLite database.

Step 7 — Return to Menu

After an operation is completed, the application returns to the main menu because the menu is inside the while True loop.

The user can perform another operation without restarting the program.

Step 8 — Exit

When the user selects option 6:

break

terminates the while True loop.

The application then displays:

Thank you for using Student Expense Tracker!

and terminates.

12. Data Flow

The general data flow is:

User
  │
  ▼
main.py
  │
  ▼
validation.py
  │
  ▼
crud.py
  │
  ▼
database.py
  │
  ▼
SQLite Database

For example, when adding an expense:

User enters expense
        ↓
main.py receives input
        ↓
validation.py validates input
        ↓
crud.py executes INSERT query
        ↓
SQLite stores the record
        ↓
Success message displayed
        ↓
Return to menu
13. Security and Good Practices

The project follows several basic programming and database best practices.

Parameterized SQL Queries

SQL queries use placeholders such as:

WHERE id = ?

instead of directly inserting user input into SQL statements.

This separates SQL commands from user-provided values.

Database Connections Are Closed

Database connections are closed inside finally blocks.

Input Validation

User input is validated before database operations are performed.

Modular Design

Different responsibilities are separated into different files:

Application control → main.py
Database operations → crud.py
Database setup → database.py
Validation → validation.py

This makes the project easier to understand and maintain.

14. Error Handling

The application handles common input and database errors.

Examples include:

Empty description
Empty category
Invalid amount
Negative amount
Invalid expense ID
Invalid date
Non-existent expense ID
Database operation errors

Instead of immediately terminating, the application displays an appropriate message and allows the user to continue.

15. Running the Application

Make sure Python 3 is installed.

From the project directory, run:

python main.py

The database and required table are created automatically.

No external Python packages are required because the project uses Python's standard library.

16. Testing Checklist

The following operations should be tested before using or submitting the application:

Add
Add a valid expense.
Try an empty description.
Try an empty category.
Try an invalid amount.
Try a negative amount.
Try an invalid date.
View
View expenses when the database is empty.
View expenses after adding records.
Search
Search using a description.
Search using a category.
Search for a value that does not exist.
Update
Update an existing expense.
Try updating a non-existent ID.
Enter invalid values during an update.
Delete
Delete an existing expense.
Try deleting a non-existent ID.
View the records afterward to confirm deletion.
17. Limitations

The current version is intentionally a simple CLI application.

Current limitations include:

No graphical user interface
No user authentication
No cloud database
No expense charts or reports
No CSV export
No web interface
No multi-user functionality

These features can be considered for future versions.

18. Future Enhancements

Possible future improvements include:

Add monthly and category-wise expense summaries.
Add CSV export functionality.
Add graphical reports and charts.
Develop a web interface using Flask or FastAPI.
Add user authentication.
Add filtering by date range.
Add budget tracking.
Add a graphical user interface.
19. Conclusion

The Student Expense Tracker demonstrates how Python can be combined with SQLite to build a practical database-driven CLI application.

The project implements complete CRUD functionality, input validation, exception handling, SQL queries, and modular Python programming.

It provides a foundation that can later be extended into a larger expense management system with reporting, visualization, authentication, or a web interface.