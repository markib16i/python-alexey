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
        if board[x_int - 1][y_int - 1] == ' ':
            board[x_int - 1][y_int - 1] = whos_turn
            break
        else:
            print("This place is full.")

    has_won = False

    # проверить, не победил ли этот игрок
    # x_int, y_int
    # whos_turn
    if board[x_int - 1] == [whos_turn] * width:
        has_won = True

    else:
        has_won = True
        # проверяем вертикаль
        for row in board:
            if row[y_int - 1] != whos_turn:
                has_won = False
                break
        if has_won == False:
            has_won = True
            # проверяем диагональ
            for i in range(height):
                if board[i][i] != whos_turn:
                    has_won = False
                    break
            if has_won == False:
                has_won = True
                # проверяем другую диагональ
                for i in range(height):
                    if board[i][-i - 1] != whos_turn:
                        has_won = False
                        break

    # после всех проверок, если флаг поднят, объявим победителя
    if has_won:
        print("Player", whos_turn, "has won!")
        break


# Домашка:

# 1. Печатать финальную позицию по окончании игры.
# 2. Объявлять ничью, если все клетки заполнены, а победителя нет.
