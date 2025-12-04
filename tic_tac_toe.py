# Наше игровое поле 3*3
#    0 1 2
# 0: . . .
# 1: . . .
# 2: . . .

# . . .
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]
max_turns = len(board) * len(board[0])

# main game loop
for turn_number in range(1, max_turns + 1):
    is_it_x_turn = turn_number % 2 == 1
    # Homework:
    # Печатать номер хода
    # Печатать, чей ход (X или 0)

    print("it is",is_it_x_turn)
    for row in board:
        print('|' + '|'.join(row) + '|')

    # Homework:
    # Пригласить ввести координаты для очередного хода

#     1 2 3
#  1 | | | |
#  2 | |X| |
#  2 |0| | |