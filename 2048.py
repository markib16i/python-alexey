import random
from shutil import move


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
    our_question = "Enter the coordinates of the tile you want to push and the direction (w/a/s/d): "
    player_answer = input(our_question)

    row_number, column_number, direction = player_answer.split()
    row_index = int(row_number) - 1
    column_index = int(column_number) - 1

    # remember choice
    new_row_index =     row_number
    new_column_index = column_number

    # Try to move further - according to user choice
    while True:
        # save new before move
        new_before_row_index = new_row_index
        new_before_column_index = new_column_index

        # update new by move
        match direction:
            # up
            case "w":
                new_row_index -= 1
            # bottom
            case "s":
                new_row_index += 1
            # left
            case 'a':
                new_column_index -= 1
            # right
            case "d":
                new_column_index += 1

        # 1. А есть ли тут такой же тайл
        if board[new_row_index][new_column_index] == board[current_row_index][current_column_index]:
            board[new_row_index][new_column_index] *= 2
            break

        # 2. А есть ли тут другой тайл


        # 3. А НЕ ДОШЛИ ЛИ МЫ ДО КРАЯ
        if 0 < new_row_index < 4 and 0 < new_column_index < 3:
            board[new_row_index][new_column_index] = board[current_row_index][current_column_index]
            board[current_row_index][current_column_index] = None
            break





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