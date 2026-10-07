# Student Expense Tracker

A Python-based Command Line Interface (CLI) application for managing and tracking student expenses using SQLite.

The application allows users to add, view, search, update, and delete expense records through a simple terminal-based menu.

## Project Overview

The Student Expense Tracker is designed to provide a simple way for students to record and manage their daily expenses.

The project uses **Python** for application logic and **SQLite** for persistent data storage. It follows a modular structure where database operations, validation, and application control are separated into different Python files.

The application implements complete **CRUD operations**:

- **Create** — Add a new expense
- **Read** — View all stored expenses
- **Update** — Modify an existing expense
- **Delete** — Remove an expense

It also provides a search feature to find expenses by description or category.

## Features

- Add new expenses
- View all recorded expenses
- Search expenses by description or category
- Update existing expenses using their ID
- Delete expenses using their ID
- Validate required text fields
- Validate positive expense amounts
- Validate expense IDs
- Validate dates in `YYYY-MM-DD` format
- Store expense records permanently using SQLite
- Automatically create the database and expenses table
- Handle invalid user input without terminating the application
- Simple and easy-to-use command-line interface

## Technologies Used

- **Python 3**
- **SQLite**
- **SQL**
- **Git & GitHub**

### Python Modules Used

The project uses Python's built-in modules:

- `sqlite3` — SQLite database operations
- `pathlib` — File and directory path handling
- `datetime` — Date validation

No external Python packages are required.

## Database Structure

The application uses an SQLite database named `expenses.db`.

The `expenses` table contains the following fields:

| Field | Type | Description |
|---|---|---|
| `id` | INTEGER | Unique expense ID |
| `description` | TEXT | Description of the expense |
| `category` | TEXT | Expense category |
| `amount` | REAL | Expense amount |
| `date` | TEXT | Expense date |

The `id` field is automatically generated using SQLite's `AUTOINCREMENT`.

## Project Structure

```text
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
Setup
1. Clone the Repository
git clone https://github.com/YOUR-USERNAME/student-expense-tracker-sqlite.git

Replace YOUR-USERNAME with your GitHub username.

2. Open the Project Directory
cd student-expense-tracker-sqlite
3. Check Python Installation

Make sure Python 3 is installed:

python --version

The project is designed to work with Python 3.

4. Install Dependencies

This project uses only Python standard-library modules, so no external packages are required.

You can still use:

pip install -r requirements.txt

if the requirements file is provided.

Usage

Run the application using:

python main.py

The application displays a menu:

1. Add Expense
2. View All Expenses
3. Search Expense
4. Update Expense
5. Delete Expense
6. Exit
Add Expense

Select option 1 and enter:

Expense description
Category
Amount
Date

Example:

Enter expense description: Bus Ticket
Enter expense category: Travel
Enter expense amount: 50
Enter expense date (YYYY-MM-DD): 2026-10-06
View Expenses

Select option 2 to display all stored expenses.

Search Expense

Select option 3 to search for an expense using its description or category.

Update Expense

Select option 4, enter the expense ID, and provide the updated information.

Delete Expense

Select option 5, enter the expense ID, and delete the corresponding record.

Exit

Select option 6 to safely exit the application.

Input Validation

The application validates user input before storing data in the database.

Examples of validation include:

Empty descriptions and categories are rejected.
Amounts must be valid positive numbers.
Expense IDs must be positive integers.
Dates must follow the YYYY-MM-DD format.

Invalid input prompts the user to enter the information again instead of terminating the program.

Database

The application automatically creates the following database path:

data/expenses.db

If the database or expenses table does not exist, it is created automatically when the application starts.

The database file is intentionally excluded from Git because it contains locally generated application data.

Learning Outcomes

This project helped develop practical understanding of:

Python functions
Modular programming
Exception handling
File and path handling
SQLite database operations
SQL queries
CRUD operations
Parameterized SQL queries
Input validation
Command Line Interface development
Git and GitHub project management
Future Improvements

Possible future enhancements include:

Expense summary and total spending reports
Monthly expense analysis
Category-wise spending reports
Export expenses to CSV
Graphical user interface
Web-based version
User authentication
Author

Sayyed Hafeeja Sulthana

B.Tech Student | Aspiring Software Developer & Full Stack Developer

GitHub: https://github.com/25A31A05HF