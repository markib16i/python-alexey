# ask user
rows = int(input("how many rows? "))
columns = int(input("how many columns? "))

# build a line to be printed in each row
numbers = ""
for item in range(columns):
    numbers = numbers + " " + str(item)

# print the line for each row
for item in range(rows):
    print(numbers)