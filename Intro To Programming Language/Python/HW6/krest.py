# Задача 1. Создайте программу для игры в "Крестики-нолики".
import random
import time


def play_game():
    print('play_game')
def game_init():
    print('game_init')

def print_table(table):
    for item in table:
        print(item)
def my_step():
    print('my_step')

def bot_step(table):
    x = random.randint(0, 2)
    y = random.randint(0, 2)
    while table[x][y] == '0' or table[x][y] == 'x':
        x = random.randint(0, 2)
        y = random.randint(0, 2)
    time.sleep(2)
    return x, y


table = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
#     command = input('\nВаше действие, введите поле x,y (3,3): ')
for i in range(9):
    x, y = map(int, input('\nчерез запятую введите строку и столбец (3х3): ').split(','))
    table[x-1][y-1] = 'х'
    print_table(table)

    x,y = bot_step(table)
    table[x][y] = '0'
    print_table(table)

