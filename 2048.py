board = [
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
    [None, None, None, None],
]
import random

def random_number():
    # var 1
    # return random.sample([2, 2, 2, 2, 2, 2, 2, 2, 2, 4], 1)[0]

    # var 2
    if random.randint(0, 9) == 0:
        return 4
    else:
        return 2

# Домашка

# Дописать функцию random_number так, чтобы она возвращала либо 2, либо 4 с вероятностью 90% и 10% соответственно.