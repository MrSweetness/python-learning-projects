import datetime
import os

expenseFilePath = "c:\dev\junk\expenses.txt"

def validateExpenseAmountEntry():
    while True:
        try:
            expenseAmount = float(input("Enter the expense amount: "))
            if expenseAmount <= 0:
                print("Expense amount must be greater than 0.")
                continue
            return expenseAmount
        except ValueError:
            print("Invalid input. Please enter a numeric value for the expense amount.")

def validateIsNotDuplicateExpense(expenseDescr, expenseAmount, expenseDate):
    # Check if the file exists
    if os.path.exists(expenseFilePath):
        with open(expenseFilePath, "r") as file:
            for line in file:
                # Split the line into components
                descr, amount, date = line.strip().split(",")
                # Check if the expense already exists
                if descr == expenseDescr and float(amount) == expenseAmount and date == expenseDate.strftime('%Y-%m-%d'):
                    return True  # Duplicate found
    return False  # No duplicates

def trackExpense(expenseDescr, expenseAmount, expenseDate):
    print(f"Tracking expense: {expenseDescr}, Amount: {expenseAmount}, Date: {expenseDate.strftime('%Y-%m-%d')}")
    # save to file
    try:
        with open(expenseFilePath, "a") as file:
            file.write(f"{expenseDescr},{expenseAmount},{expenseDate.strftime('%Y-%m-%d')}\n")
    except Exception as e:
        print(f"Error saving expense: {e}")
        # Handle the error (e.g., log it, notify the user, etc.)
        # For now, just print the error message
    pass

def viewTrackedExpenses():
    # Check if the file exists
    if os.path.exists(expenseFilePath):
        with open(expenseFilePath, "r") as file:
            print("Tracked Expenses:")
            for line in file:
                print(line.strip())
    else:
        print("No expenses tracked yet.")

while True:
    print("--------------------------------------------")
    print("Welcome to the Expense Tracker!")
    print("1. View tracked expenses")
    print("2. Add a new expense")
    print("3. Exit")
    choice = input("Please choose an option (1-3): ").strip()

    if choice == '1':
        viewTrackedExpenses()
        continue
    elif choice == '2':
        expenseDescr = input("Enter the expense description: ")
        expenseAmount = validateExpenseAmountEntry()
        
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
    elif choice == '3':
        print("Exiting the expense tracker.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
        continue
        
"""
TODO List:
- Add functionality to edit or delete existing expenses.
- Implement a summary feature to calculate total expenses for a given period.
- Add a feature to categorize expenses (e.g., food, transport, entertainment).
- Implement a user-friendly interface (e.g., using a GUI library or web framework).
"""