
from database import create_table
from crud import (
    add_expense,
    get_all_expenses,
    search_expenses,
    update_expense,
    delete_expense,
    expense_exists
)
from validation import (
    validate_non_empty,
    validate_amount,
    validate_id,
    validate_date
)


def main():
    create_table()

    print("=" * 50)
    print("        STUDENT EXPENSE TRACKER")
    print("=" * 50)

    while True:
        print("\n1. Add Expense")
        print("2. View All Expenses")
        print("3. Search Expense")
        print("4. Update Expense")
        print("5. Delete Expense")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        # ---------------- ADD EXPENSE ----------------
        if choice == "1":
            print("\n--- Add Expense ---")

            description = input("Enter expense description: ").strip()

            while not validate_non_empty(description, "Description"):
                description = input("Enter expense description: ").strip()

            category = input("Enter expense category: ").strip()

            while not validate_non_empty(category, "Category"):
                category = input("Enter expense category: ").strip()

            amount_input = input("Enter expense amount: ").strip()
            amount = validate_amount(amount_input)

            while amount is None:
                amount_input = input("Enter expense amount: ").strip()
                amount = validate_amount(amount_input)

            date_input = input(
                "Enter expense date (YYYY-MM-DD): "
            ).strip()

            date = validate_date(date_input)

            while date is None:
                date_input = input(
                    "Enter expense date (YYYY-MM-DD): "
                ).strip()

                date = validate_date(date_input)

            add_expense(
                description,
                category,
                amount,
                date
            )

        # ---------------- VIEW EXPENSES ----------------
        elif choice == "2":
            print("\n--- View Expenses ---")
            get_all_expenses()

        # ---------------- SEARCH EXPENSE ----------------
        elif choice == "3":
            print("\n--- Search Expense ---")

            search_term = input(
                "Enter description or category to search: "
            ).strip()

            while not validate_non_empty(search_term, "Search term"):
                search_term = input(
                    "Enter description or category to search: "
                ).strip()

            search_expenses(search_term)

        # ---------------- UPDATE EXPENSE ----------------
        elif choice == "4":
            print("\n--- Update Expense ---")

            id_input = input(
                "Enter expense ID to update: "
            ).strip()

            expense_id = validate_id(id_input)

            while expense_id is None:
                id_input = input(
                    "Enter expense ID to update: "
                ).strip()

                expense_id = validate_id(id_input)

            # Check whether the expense exists
            if not expense_exists(expense_id):
                print("Expense not found.")
                continue

            description = input(
                "Enter new description: "
            ).strip()

            while not validate_non_empty(description, "Description"):
                description = input(
                    "Enter new description: "
                ).strip()

            category = input(
                "Enter new category: "
            ).strip()

            while not validate_non_empty(category, "Category"):
                category = input(
                    "Enter new category: "
                ).strip()

            amount_input = input(
                "Enter new amount: "
            ).strip()

            amount = validate_amount(amount_input)

            while amount is None:
                amount_input = input(
                    "Enter new amount: "
                ).strip()

                amount = validate_amount(amount_input)

            date_input = input(
                "Enter new date (YYYY-MM-DD): "
            ).strip()

            date = validate_date(date_input)

            while date is None:
                date_input = input(
                    "Enter new date (YYYY-MM-DD): "
                ).strip()

                date = validate_date(date_input)

            update_expense(
                expense_id,
                description,
                category,
                amount,
                date
            )

        # ---------------- DELETE EXPENSE ----------------
        elif choice == "5":
            print("\n--- Delete Expense ---")

            id_input = input(
                "Enter expense ID to delete: "
            ).strip()

            expense_id = validate_id(id_input)

            while expense_id is None:
                id_input = input(
                    "Enter expense ID to delete: "
                ).strip()

                expense_id = validate_id(id_input)

            delete_expense(expense_id)

        # ---------------- EXIT ----------------
        elif choice == "6":
            print("\nThank you for using Student Expense Tracker!")
            break

        # ---------------- INVALID CHOICE ----------------
        else:
            print(
                "\nInvalid choice. Please enter a number from 1 to 6."
            )


if __name__ == "__main__":
    main()

