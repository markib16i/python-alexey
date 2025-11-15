#player_number = int(input("enter a number from 1 to 100. "))
min = 1
max = 100
for i in range(min, max):
    player_answer = input("is it " + str(i) +"?")
    if player_answer == "n":
        continue
    elif player_answer == "y":
        print("I WON! Your number is",i)
        break
