from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time in a formatted string."""
    current_datetime = datetime.now()
    current_date = current_datetime.date()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")

def calculate_future_date():
    """Calculates and displays a future date based on user input."""
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    current_datetime = datetime.now()
    future_date = current_datetime + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()