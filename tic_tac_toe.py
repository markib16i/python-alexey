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
width = len(board[0])
height = len(board)
max_turns = width * height

# main game loop
for turn_number in range(1, max_turns + 1):
    if turn_number % 2 == 1:
        whos_turn = 'X'
    else:
        whos_turn = '0'

    # номер хода
    print("It is turn №", turn_number)

    # чей ход
    print("It is", whos_turn, "'s turn")

    # рисуем доску
    print('  ', end='')
    for i in range(width):
        print('  ', i + 1, end='')
    print()
    print('   ' + '-' * (width * 4 + 1))
    for row_number, row in enumerate(board):
        print(row_number + 1, ' | ' + ' | '.join(row) + ' |')
        print('   ' + '-' * (width * 4 + 1))


    # игрок делает ход
    while ...:
        player_coordinates = input("Where will you put your symbol? ")
        # "1 1"  "2 1" "3 2"
        x, y = player_coordinates.split()
        x_int = int(x)
        y_int = int(y)
        if board[x_int - 1][y_int - 1] is ' ':
            board[x_int - 1][y_int - 1] = whos_turn
            break
        else:
            print("This place is full.")

    # проверить, не победил ли этот игрок
    # x_int, y_int
    # whos_turn


    has_won = False
    # проверим ряд x_int
    #    все ячейки в ряду равны whos_turn
    if board[x_int - 1] == [whos_turn] * width:
        has_won = True
    else:
        # проверим колонку y_int (не работает?)
        #    все ячейки в колонке равны whos_turn
        has_won = True
        for row in board:
            if row[y_int - 1] != whos_turn:
                has_won = False
                break
        # проверим диагонали (2 варианта)
        for i in range(height):
            if board[i][i] != whos_turn :
                has_won = False
                break

    # после всех проверок, если флаг поднят, объявим победителя
    if has_won:
        print("Player", whos_turn, "has won!")
        break





#     1   2   3
#   -------------
# 1 | X | X | X |
#   -------------
# 2 | 0 | 0 | 0 |
#   -------------
# 3 | 8 | 8 | 8 |
#   -------------