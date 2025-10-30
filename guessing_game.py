import random

# Computer generates a random number between 1 and 100
computer_number = random.randint(1, 100)

while True:
    # Player tries to guess the number
    players_guess = int(input("Which number I have chosen? "))
    if players_guess > computer_number:
        print("Your number is greater than mine. ")
    elif players_guess < computer_number:
        print("Your number is lesser than mine. ")
    else:
        print("You won!")
        break
    # If the guess is too high or too low, the computer provides feedback

    # Or if the guess is correct, the computer congratulates the player
