board = [
    [' ',' ',' '],
    [' ',' ',' ',' '],
    [' ',' ',' '],
]
total = 0
number = 0
for row in board:
    total += len(row)
    number += 1
    print("line", number, "has", len(row), "elements")
print("total:", total, "elements")
