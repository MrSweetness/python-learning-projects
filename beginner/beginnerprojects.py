import random

supportedFunctions = ["calculator", "guessingGame"]

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

###########################################################################################
# Main function
###########################################################################################

def main(funcSelection):
    if funcSelection == "calculate" or "calculator":
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter the operator (+, -, *, /): ")
        answer = calculate(num1, num2, operator)
        print(answer)
    elif funcSelection == "guessingGame":
        guessingGame()

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