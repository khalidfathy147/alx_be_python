def daily_reminder():
    """
    This function takes user input for a single task, priority, and time sensitivity
    and provides a customized reminder message.
    """

    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            reminder = "Reminder: '" + task + "' is a high priority task "
        case "medium":
            reminder = "Reminder: '" + task + "' is a medium priority task "
        case "low":
            reminder = "Reminder: '" + task + "' is a low priority task "
        case _:
            reminder = "Reminder: '" + task + "' is a task "

    if time_bound == "yes":
        reminder += "that requires immediate attention today!"
    else:
        reminder += ". Consider completing it when you have free time."

    print(f"{reminder}")  #  The f-string is essential here!


if __name__ == "__main__":
    daily_reminder()