import datetime
import time
import random
import winsound

supportedFunctions = ["calculator", "toDoList", "guessingGame", "alarmClock", "passwordGenerator", "rockPaperScissors"]
taskList = {}

def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    else:
        return "Invalid operator"
    
def toDoList():
    while True:
        print("---To-Do List Menu:---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Update task status")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Tasks:")
            for task in taskList:
                print("-", task, ":", taskList[task])
        elif choice == 2:
            task = input("Enter the task: ")
            taskList[task] = "Incomplete"
        elif choice == 3:
            task = input("Enter the task to remove: ")
            if task in taskList:
                del taskList[task]
            else:
                print("Task not found")
        elif choice == 4:
            task = input("Enter the task to update: ")
            if task in taskList:
                status = input("Enter the status (Complete/Incomplete): ")
                taskList[task] = status
            else:
                print("Task not found")
        elif choice == 5:
            break
    
def guessingGame():
    number = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = int(input("Enter a number between 1 and 100: "))
        attempts += 1
        
        if guess < number:
            print("Too low")
        elif guess > number:
            print("Too high")
        else:
            print("Correct! It took you", attempts, "attempts")
            break

def alarmClock(alarmTime):
    currentTime = datetime.datetime.now()

    timeDifference = (alarmTime - currentTime).total_seconds()

    if timeDifference < 0:
        print("Invalid time. Please enter a time in the future")

    print("Alarm set for:", alarmTime)
    
    time.sleep(timeDifference)

    #TODO: Replace with system agnostic method, currently windows only
    #TODO: Add ability to hold alarm and allow for other functions to be run
    # Play alarm sound (beep at 1000Hz for 2 seconds)
    print("ALARM! WAKE UP!")
    duration = 2000  # milliseconds
    freq = 1000  # Hz
    
    # Repeat beep 3 times
    for _ in range(3):
        winsound.Beep(freq, duration)
        time.sleep(0.5)


def passwordGenerator(passwordLength):
    password = ""

    passCharacters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                      "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                      "$", "@", "#", "&", "*", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in range(passwordLength):
        password += str(random.choice(passCharacters))

    return password

def rps():
    while True:
        userChoice = input("Enter rock, paper, or scissors: ")
        choices = ["rock", "paper", "scissors"]
        computerChoice = random.choice(choices)

        if userChoice == computerChoice:
            print("It's a tie!")
        elif userChoice == "rock":
            if computerChoice == "paper":
                print("You lose! Paper covers rock")
            else:
                print("You win! Rock smashes scissors")
        elif userChoice == "paper":
            if computerChoice == "rock":
                print("You win! Paper covers rock")
            else:
                print("You lose! Scissors cuts paper")
        elif userChoice == "scissors":
            if computerChoice == "rock":
                print("You lose! Rock smashes scissors")
            else:
                print("You win! Scissors cuts paper")
        else:
            print("Invalid input")
        
        playAgain = input("Do you want to play again? (yes/no): ")
        if playAgain == "no":
            break
        else:
            continue

###########################################################################################
# Main function
###########################################################################################

def main(funcSelection):
    if funcSelection == "calculator":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        answer = calculate(num1, num2, operator)
        print(answer)
    elif funcSelection == "guessingGame":
        guessingGame()
    elif funcSelection == "passwordGenerator":
        passwordLength = int(input("Enter the desired length of the password: "))
        print("Your password is:", passwordGenerator(passwordLength))
    elif funcSelection == "rockPaperScissors":
        rps()
    elif funcSelection == "alarmClock":
        # Get user input for alarm time
        alarm_input = input("Enter alarm time (YYYY-MM-DD HH:MM:SS): ")
        try:
            alarmTime = datetime.datetime.strptime(alarm_input, "%Y-%m-%d %H:%M:%S")
            alarmClock(alarmTime)
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD HH:MM:SS")
    elif funcSelection == "toDoList":
        toDoList()

while True:
    userInput = input("Enter a function name or 'quit' to exit. Enter help to get more info: ")
    
    if userInput == "quit":
        break
    elif userInput == "help":
        print("Supported functions:")
        for func in supportedFunctions:
            print("-" + func)
    elif userInput in supportedFunctions:
        main(userInput)
    else:
        print("Invalid function name")