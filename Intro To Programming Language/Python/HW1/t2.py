# not (x|y|z) == (not x & not y & noy z)

from random import randint, random


def is_true(x, y, z):
    if (not (x | y | z) == (not x) & (not y) & (not z)):
        return True


def create_random_list():
    l = list(randint(-10, 10) for x in range(3))
    return l


def create_from_keyb_list():
    s = list(map(int, input('введите три числа через пробел: ').split()))
    return s


s = create_random_list()
print(s)
print(is_true(s[0], s[1], s[2]))
