import datetime
import os

def trackExpense(expenseDescr, expenseAmount, expenseDate):
    print(f"Tracking expense: {expenseDescr}, Amount: {expenseAmount}, Date: {expenseDate.strftime('%Y-%m-%d')}")
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
                date_obj = datetime.strptime(expenseDate, "%Y-%m-%d").date()
                #year, month, day = map(int, expenseDate.split('-'))
                #if not (1 <= month <= 12 and 1 <= day <= 31 and len(str(year)) == 4):
                #    raise ValueError("Invalid date")
                expenseDateValid = True
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
                continue

        trackExpense(expenseDescr, expenseAmount, date_obj)
        print("Expense added successfully!")
    elif userChoice == 'no':
        print("Exiting the expense tracker.")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
# Note: The trackExpense function is a placeholder and does not actually save the expense.

"""
TODO List:
- Implement the trackExpense function to save the expense to a file or database.
- Add error handling for invalid inputs (e.g., non-numeric expense amount).
- Implement a way to view all tracked expenses.
- Add functionality to edit or delete existing expenses.
- Implement a summary feature to calculate total expenses for a given period.
- Add a feature to categorize expenses (e.g., food, transport, entertainment).
- Implement a user-friendly interface (e.g., using a GUI library or web framework).
"""