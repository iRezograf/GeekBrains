# Задача 1. Создайте программу для игры в "Крестики-нолики".
import random
import time

PLAYER_ONE = 'X'
PLAYER_TWO = '0'
INIT_SYMBOL = '-'


def play_game():
    print('play_game')


def game_init():
    print('game_init')


# def is_win(who):
#     for j in range(3):
#         win = True
#         for i in range(3):
#             win = True and table[i][j] == who
#         if win:
#             return win
#         return 0
#

def print_table(table):
    for item in table:
        print(item)


def my_step():
    print('my_step')


def init_table(table, who):
    # инициализация таблицы знеченими who
    for row in range(len(table[0])):
        for col in range(len(table[1])):
            table[row][col] = who

    #print(table)

def win_cases(table, who):
    # проверка / диагонали
    win = True
    for row in range(len(table[0])):
        for col in range(len(table[1])):
            if row == 2 - col:
                if not (table[row][col] == who and win):
                    win = win and False
    if win:
        return win
    # проверка \ диагонали
    win = True
    for row in range(len(table[0])):
        for col in range(len(table[1])):
            if row == col:
                if not (table[row][col] == who and win):
                    win = win and False
    if win:
        return win
    # проверка строк
    for i in range(len(table[0])):
        win = True
        for row in range(len(table[0])):
            for col in range(len(table[1])):
                if not (table[i][col] == who and win):
                    win = win and False
        if win:
            return win
    # проверка столбцов
    for i in range(len(table[0])):
        win = True
        for row in range(len(table[0])):
            for col in range(len(table[1])):
                if not (table[row][i] == who and win):
                    win = win and False
        if win:
            return win
    return False


def my_step():
    print('my_step')


def bot_step(table):
    x = random.randint(0, len(table[0]) - 1)
    y = random.randint(0, len(table[1]) - 1)
    while table[x][y] == PLAYER_ONE or table[x][y] == PLAYER_TWO:
        x = random.randint(0, len(table[0]) - 1)
        y = random.randint(0, len(table[1]) - 1)
    time.sleep(2)
    return x, y


def create_init_table(power, who):
    # инициализация таблицы знеченими who
    table = []
    result = []
    for row in range(power):
        table.append(who)
    for col in range(power):
        result.append(table)

    return result
def have_free_cell(table,who):
    for i in table:
        for j in i:
            if j == who:
                #print(j)
                return True
    return False


table = [[INIT_SYMBOL] * 3 for i in range(3)]
print_table(table)

for i in range(8):
    who = PLAYER_ONE
    try:
        x, y = map(int, input('\nчерез запятую введите строку и столбец (3х3): ').split(','))
        while table[x-1][y-1] == PLAYER_ONE or table[x-1][y-1] == PLAYER_TWO:
            print('поле уже занято ...')
            x, y = map(int, input('\nчерез запятую введите строку и столбец (3х3): ').split(','))
    except:
        print("неверно введены значения")
        break
    table[x - 1][y - 1] = PLAYER_ONE
    print_table(table)
    win = win_cases(table, who)
    if win:
        print(f'Победил {who}')
        break
    print()

    who = PLAYER_TWO
    if not have_free_cell(table, INIT_SYMBOL):
        break
    x, y = bot_step(table)
    table[x][y] = PLAYER_TWO
    print_table(table)
    win = win_cases(table, who)
    if win:
        print(f'Победил {who}')
        break

if not win:
    print('Ничья ...')
