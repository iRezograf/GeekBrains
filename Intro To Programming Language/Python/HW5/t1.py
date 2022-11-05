
""" Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. 
Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. 
За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, 
чтобы забрать все конфеты у своего конкурента?

Делаем игру против бота
а) Подумайте как наделить бота ""интеллектом"" 
"""

import json
import random
import time
from tkinter import dialog
candy = {'0': 'конфет',
         '1': 'конфета',
         '2': 'конфеты',
         '3': 'конфеты',
         '4': 'конфеты',
         '5': 'конфет',
         '6': 'конфет',
         '7': 'конфет',
         '8': 'конфет',
         '9': 'конфет',
         '10': 'конфет',
         '11': 'конфет',
         '12': 'конфет',
         '13': 'конфет',
         '14': 'конфет',
         '15': 'конфет',
         '16': 'конфет',
         '17': 'конфет',
         '18': 'конфет',
         '19': 'конфет',
         }

CANDY_CNT = 51  # по заданию 2021
MAX_TAKE = 12   # по заданию 28
# выиграшная позиция: на столе у противника 28*N +1 конфета
me_have = 0
bot_have = 0
in_bot = 1
in_game = 1
bot_power = {"/weak": "тупой",
             "/middle": "не без задатков", "/diabolo": "просто чёрт"}
power = '/weak'
bank = CANDY_CNT
bot_remarks = []
#bot_remarks =["привет", "до свидания"]


wining_str = 'всем спасибо, все свободны'


def candys(num):
    return candy[str(num % 20)]


def win(cnt):
    if cnt <= 0:
        return True


def print_power_choice():
    for key, val in bot_power.items():
        print(key, ":", val)
    return input('ваше действие: ')


def my_step():
    global me_have, bank, in_bot, in_game
    print(f'\nНа столе: {str(bank)} {candys(bank)}\n')
    i = int(input('сколько конфет я забираю? :'))
    while i > MAX_TAKE or i < 1:
        i = int(input(f'Напоминаю - диапазон от 1 до {MAX_TAKE}:'))

    me_have += i
    bank -= i
    if win(bank):
        print('всем спасибо, все свободны')
        print(f'{CANDY_CNT} {candys(CANDY_CNT)} - мои!')
        in_bot = 1
        in_game = 0
    return in_game


def bot_step(power):
    global bot_have, bank, in_bot, in_game, bot_remarks
    time.sleep(0.5)
    print('Bot: ' + random.choice(bot_remarks))
    print(f'\nНа столе: {str(bank)} {candys(bank)}\n')
    if power == 0:
        i = random.randint(1, MAX_TAKE)
    if power == 3:
        if bank <= MAX_TAKE:
            i = bank
        elif bank % (MAX_TAKE + 1) > 1:
            i = bank % MAX_TAKE - 1
        elif bank % (MAX_TAKE + 1) == 1:
            i = 1
    if power == 6:
        if bank % (MAX_TAKE + 1) == 0:
            i = random.randint(1, MAX_TAKE)
        else:
            i = bank % (MAX_TAKE + 1)
    if bank <= MAX_TAKE:
        i = bank

    print(f'Решение Бота:  {str(i)}  {candys(i)}\n')
    bot_have += i
    bank -= i
    if win(bank):
        print('Бот: "За AI будущее и все ништяки!"')
        print(f'{CANDY_CNT} {candys(CANDY_CNT)} - мои!')
        in_bot = 1
        in_game = 0
    return in_game


def play_game(who_start, power):
    global me_have, bot_have, bank, in_bot, in_game
    while in_game:
        if who_start == 0:
            if not my_step():
                break
            if not bot_step(power):
                break
        if who_start == 1:
            if not bot_step(power):
                break
            if not my_step():
                break
        print(
            f'У меня: {me_have} {candys(me_have)} У бота: {bot_have} {candys(bot_have)}')


def save(save_mode):
    with open('dialog.json', mode=save_mode, encoding='utf-8') as file:
        file.write(json.dumps(bot_remarks, ensure_ascii=False))


def load(l_file):
    with open(l_file, mode='r', encoding='utf-8') as file:
        lst = json.load(file)
    return lst


#save ('w')
bot_remarks = load('dialog.json')
#print (list)
help = load('help.json')


who_start = random.randint(0, 1)
power = 0
while in_bot:
    for item in help:
        print(item)
    command = input('ваше действие: ')
    """ command = '/start'
    who_start = 1
    power = 6 """
    if command == '/0':
        who_start = 0
    if command == '/1':
        who_start = 1
    if command == '/6':
        who_start = 1
        power = 6
        #play_game(who_start, power)
    if command == '/power':
        print_power_choice()
        if command == '/weak':
            power = 0
        if command == '/middle':
            power = 3
        if command == '/diabolo':
            power = 6
            who_start = 1
    if command == '/start':
        play_game(who_start, power)
    if command == '/stop':
        break
    if command == '/h':
        for item in help:
            print(item)
    else:
        #in_bot = in_game = False
        print("")
