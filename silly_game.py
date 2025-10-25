while True:
    # Player names a number
    player_number = int(input('Enter a number: '))
    # Computer adds 6
    computer_number = 6 + player_number
    # Computer tells its number and wins
    print('My number is:', computer_number, 'I WON!')
    # loop over the above

    # Ask the player if they want to continue
    player_answer = input("Do you want to play again? (y/n): ")

    # If yes, continue the loop
    if player_answer == 'y':
        print("Let's play again then")
        continue
    else:
        # If no, break the loop
        print('OK then bye')
        break