def validate_non_empty(value, field_name):
    """Check that a text value is not empty."""
    if not value.strip():
        print(f"{field_name} cannot be empty.")
        return False

    return True


def validate_amount(value):
    """Check that the amount is a valid positive number."""
    try:
        amount = float(value)

        if amount <= 0:
            print("Amount must be greater than zero.")
            return None

        return amount

    except ValueError:
        print("Amount must be a valid number.")
        return None


def validate_id(value):
    """Check that the ID is a valid positive integer."""
    try:
        expense_id = int(value)

        if expense_id <= 0:
            print("ID must be greater than zero.")
            return None

        return expense_id

    except ValueError:
        print("ID must be a valid number.")
        return None


from datetime import datetime


def validate_date(value):
    """Check that the date follows YYYY-MM-DD format."""
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return value

    except ValueError:
        print("Date must be in YYYY-MM-DD format.")
        return None