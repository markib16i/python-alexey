import random

def random_tile():
    if random.randint(0, 9) == 0:
        return 4
    else:
        return 2

def new_tile(board):
    while True:
        # Случайно выбираем местоположение для новой плитки и плитку
        row_index = random.randint(0, 3)
        column_index = random.randint(0 ,3)

        # if the place is full - repeat
        if board[row_index][column_index] is not None:
            continue

        board[row_index][column_index] = random_tile()
        break

board = [
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
]

new_tile(board)
new_tile(board)

while True:  # Main game loop
    # 2 3 asdw
    user_answer = input("Enter the coordinates and direction: ")
    x, y, direction = user_answer.split()
    x_int = int(x) - 1
    y_int = int(y) - 1
    while True:  # Try to move further
        match direction:
            case "w":
                x_int -= 1
            case 'a':
                y_int -= 1
            case "s":
                x_int += 1
            case "d":
                y_int += 1
        # 1. А НЕ ВЫХОДИМ ЛИ МЫ ЗА ПРЕДЕЛЫ ДОСКИ?
        if 0 <= x_int <= 3 and 0 <= y_int <= 3:
            ...
        else:
            ...

        # 2. А НЕ СТОЛКНУЛИСЬ ЛИ МЫ С ПЛИТКОЙ?
        if board[x_int][y_int] is not None:
            ...
        else:
            ...


# Совет: переименовать x_int в row_index и y_int в column_index





# Оформить этот кусочек, как функцию
# Печатаем всю доску, как есть, ряд за рядом
    for row in board:
        for cell in row:
            if cell is None:
                visual_cell = ' '
            else:
                visual_cell = cell
            print(f"| {visual_cell} ", end='')
        print("|")