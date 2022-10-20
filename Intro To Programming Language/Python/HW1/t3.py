from random import randint


def create_random_points():
    return list(randint(-10, 10) for x in range(2))


def quart_of(list):
    if (list[0] > 0 and list[1] > 0):
        print_q(list[0], list[1], 1)
    elif (list[0] < 0 and list[1] > 0):
        print_q(list[0], list[1], 2)
    elif (list[0] < 0 and list[1] < 0):
        print_q(list[0], list[1], 3)
    else:
        print_q(list[0], list[1], 4)


def print_q(x, y, n):
    print(f'x = {x} y = {y} -> {n}')


quart_of(create_random_points())
