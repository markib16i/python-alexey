player_number = int(input("Produce a number between 1 and hundred, type it here: "))
current_range_start = 1
current_range_end = 100
while True:
    current_range_middle = (current_range_start + current_range_end) // 2
    print("I think that your number is", current_range_middle)

    if player_number > current_range_middle:
        print("But looks like your number is greater. ")
        current_range_start = current_range_middle
    elif player_number < current_range_middle:
        print("But looks like your number is lesser.")
        current_range_end = current_range_middle
    else:
        print("I WON! ")
        break