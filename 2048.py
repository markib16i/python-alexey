import random
from shutil import move


def print_board(board):
    for row in board:
        for cell in row:
            if cell is None:
                visual_cell = ' '
            else:
                visual_cell = cell
            print(f"| {visual_cell} ", end='')
        print("|")

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
    print_board(board)
    our_question = "Enter the coordinates of the tile you want to push and the direction (w/a/s/d): "
    player_answer = input(our_question)

    row_number, column_number, direction = player_answer.split()
    row_index = int(row_number) - 1
    column_index = int(column_number) - 1

    # # remember choice
    # new_row_index = row_number
    # new_column_index = column_number

    # Try to move further - according to user choice
    while True:
        # set the next position to the current position
        next_row_index = row_index
        next_column_index = column_index

        # calculate next position
        match direction:
            # up
            case "w":
                next_row_index -= 1
            # bottom
            case "s":
                next_row_index += 1
            # left
            case 'a':
                next_column_index -= 1
            # right
            case "d":
                next_column_index += 1

        # А НЕ ДОШЛИ ЛИ МЫ ДО КРАЯ
        if not (
            0 <= next_row_index <= 3 and
            0 <= next_column_index <= 3
        ):
            break

        tile = board[row_index][column_index]
        destination_tile = board[next_row_index][next_column_index]

        # А есть ли тут такой же тайл
        if destination_tile == tile:
            destination_tile *= 2
            tile = None
            break

        # А есть ли тут другой тайл
        if destination_tile != None:
            break


        board[next_row_index][next_column_index] = tile
        board[row_index][column_index] = None
        row_index = next_row_index
        column_index = next_column_index

