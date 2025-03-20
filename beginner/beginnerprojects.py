import random

supportedFunctions = ["calculator", "guessingGame", "passwordGenerator"]

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

def passwordGenerator(passwordLength):
    password = ""

    passCharacters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                      "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                      "$", "@", "#", "&", "*", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in range(passwordLength):
        password += str(random.choice(passCharacters))

    return password

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