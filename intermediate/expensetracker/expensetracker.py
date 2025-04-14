import datetime
import os

def validateIsNotDuplicateExpense(expenseDescr, expenseAmount, expenseDate):
    # Check if the file exists
    if os.path.exists("c:\dev\junk\expenses.txt"):
        with open("c:\dev\junk\expenses.txt", "r") as file:
            for line in file:
                # Split the line into components
                descr, amount, date = line.strip().split(",")
                # Check if the expense already exists
                if descr == expenseDescr.lower() and amount == expenseAmount and date == expenseDate.strftime('%Y-%m-%d'):
                    return True  # Duplicate found
    return False  # No duplicates

def trackExpense(expenseDescr, expenseAmount, expenseDate):
    print(f"Tracking expense: {expenseDescr}, Amount: {expenseAmount}, Date: {expenseDate.strftime('%Y-%m-%d')}")
    # save to file
    try:
        with open("c:\dev\junk\expenses.txt", "a") as file:
            file.write(f"{expenseDescr},{expenseAmount},{expenseDate.strftime('%Y-%m-%d')}\n")
    except Exception as e:
        print(f"Error saving expense: {e}")
        # Handle the error (e.g., log it, notify the user, etc.)
        # For now, just print the error message
    pass

while True:
    userChoice = input("Do you want to add a new expense? (yes/no): ").strip().lower()
    if userChoice == 'yes':
        expenseDescr = input("Enter the expense description: ")
        expenseAmount = input("Enter the expense amount: ")
        
        expenseDateValid = False
        while expenseDateValid == False:
            expenseDate = input("Enter the date of the expense (YYYY-MM-DD): ")

            # Validate the date format (YYYY-MM-DD)
            try:
                date_obj = datetime.datetime.strptime(expenseDate, "%Y-%m-%d").date()
                expenseDateValid = True
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                continue
        
        # Check for duplicate expense
        if validateIsNotDuplicateExpense(expenseDescr, expenseAmount, date_obj):
            print("This expense already exists.")
            continue

        trackExpense(expenseDescr, expenseAmount, date_obj)
        print("Expense added successfully!")
    elif userChoice == 'no':
        print("Exiting the expense tracker.")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
# Note: The trackExpense function is a placeholder and does not actually save the expense.