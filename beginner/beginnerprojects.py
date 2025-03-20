import random

supportedFunctions = ["calculator", "guessingGame", "passwordGenerator", "rockPaperScissors"]

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