from database import get_connection


def add_expense(description, category, amount, date):
    """Add a new expense to the database."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO expenses (description, category, amount, date)
            VALUES (?, ?, ?, ?)
        """, (description, category, amount, date))

        connection.commit()

        print("Expense added successfully!")

    except Exception as e:
        print("Error adding expense:", e)

    finally:
        connection.close()
        
def get_all_expenses():
    """Retrieve and display all expenses."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, description, category, amount, date
            FROM expenses
            ORDER BY id
        """)

        expenses = cursor.fetchall()

        if not expenses:
            print("No expenses found.")
            return

        print("\n" + "=" * 70)
        print("                    ALL EXPENSES")
        print("=" * 70)

        print(f"{'ID':<5}{'Description':<20}{'Category':<15}{'Amount':<12}{'Date'}")
        print("-" * 70)

        for expense in expenses:
            print(
                f"{expense[0]:<5}"
                f"{expense[1]:<20}"
                f"{expense[2]:<15}"
                f"₹{expense[3]:<11.2f}"
                f"{expense[4]}"
            )

        print("=" * 70)

    except Exception as e:
        print("Error retrieving expenses:", e)

    finally:
        connection.close()
        
        
def search_expenses(search_term):
    """Search expenses by description or category."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT id, description, category, amount, date
            FROM expenses
            WHERE description LIKE ? OR category LIKE ?
            ORDER BY id
        """, (f"%{search_term}%", f"%{search_term}%"))

        expenses = cursor.fetchall()

        if not expenses:
            print("No matching expenses found.")
            return

        print("\n" + "=" * 70)
        print("                    SEARCH RESULTS")
        print("=" * 70)

        print(f"{'ID':<5}{'Description':<20}{'Category':<15}{'Amount':<12}{'Date'}")
        print("-" * 70)

        for expense in expenses:
            print(
                f"{expense[0]:<5}"
                f"{expense[1]:<20}"
                f"{expense[2]:<15}"
                f"₹{expense[3]:<11.2f}"
                f"{expense[4]}"
            )

        print("=" * 70)

    except Exception as e:
        print("Error searching expenses:", e)

    finally:
        connection.close()

def expense_exists(expense_id):
    """Check whether an expense ID exists."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute(
            "SELECT id FROM expenses WHERE id = ?",
            (expense_id,)
        )

        return cursor.fetchone() is not None

    except Exception as e:
        print("Error checking expense:", e)
        return False

    finally:
        connection.close()


def update_expense(expense_id, description, category, amount, date):
    """Update an existing expense."""
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE expenses
            SET description = ?,
                category = ?,
                amount = ?,
                date = ?
            WHERE id = ?
        """, (description, category, amount, date, expense_id))

        if cursor.rowcount == 0:
            print("Expense not found.")
            return

        connection.commit()

        print("Expense updated successfully!")

    except Exception as e:
        print("Error updating expense:", e)

    finally:
        connection.close()
        
def delete_expense(expense_id):
    """Delete an expense by its ID."""
    
    connection = get_connection()

    try:
        cursor = connection.cursor()

        

        cursor.execute("""
            DELETE FROM expenses
            WHERE id = ?
        """, (expense_id,))

        

        if cursor.rowcount == 0:
            print("Expense not found.")
            return

        connection.commit()

        print("Expense deleted successfully!")

    except Exception as e:
        print("Error deleting expense:", e)

    finally:
        connection.close()