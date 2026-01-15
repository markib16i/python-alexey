import random

def random_tile():
    if random.randint(0, 9) == 0:
        return 4
    else:
        return 2

def new_tile(board):
    # Случайно выбираем местоположение для новой плитки и плитку
    row_index = random.randint(0, 3)
    column_index = random.randint(0 ,3)
    # Домашка: проверить, что место не занято или повторить случайный выбор
    board[row_index][column_index] = random_tile()


board = [
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
]

new_tile(board)
new_tile(board)



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