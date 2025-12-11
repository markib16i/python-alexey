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
    player_turn = turn_number % 2 == 1

    # номер хода
    print("It is turn №", turn_number)

    # чей ход
    if player_turn == True:
        print("it is player turn")
    else:
        print("it is computer turn")

    # рисуем доску
    for row in board:
        print('|' + '|'.join(row) + '|')

    # ход игрока
    if player_turn == True:
        print("please,it is player turn")
        

    # ход компьютера
    else:
        print("my turn, ha-ha-ha")


#     1 2 3
#  1 | | | |
#  2 | |X| |
#  2 |0| | |