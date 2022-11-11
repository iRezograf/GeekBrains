
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
candy = {'0': 'конфет',
         '1': 'конфета',
         '2': 'конфеты',
         '3': 'конфеты',
         '4': 'конфеты',
         '5': 'конфет',
         '6': 'конфет',
         '7': 'конфет',
         '8': 'конфет',
         '9': 'конфет'}


CANDY_CNT = 117  # по заданию 2021
MAX_TAKE = 28   # по заданию 28
# выиграшная позиция: на столе у противника (MAX_TAKE + 1)*N конфета
me_have = 0
bot_have = 0
in_bot = 1
game_over = 0
bank = CANDY_CNT
bot_remarks = []
# bot_remarks =["привет", "до свидания"]
bot_power = {"/weak": "тупой",
             "/middle": "не без задатков", "/diabolo": "просто чёрт"}
wining_str = 'всем спасибо, все свободны'


def game_init():
    global me_have, bot_have, in_bot, game_over, bank
    me_have = 0
    bot_have = 0
    in_bot = 1
    game_over = 0
    bank = CANDY_CNT


def candys(num):
    if 10 <= int(str(num)[-2:]) <= 20:
        return 'конфет'
    else:
        return candy[str(num % 10)]


def win(cnt):
    if cnt <= 0:
        return True


def power_choice():
    for key, val in bot_power.items():
        print(key, ":", val)
    return input('Ваше действие: ')

def print_items(array):
    for item in array:
        print(item)

def my_step():
    global me_have, bank, in_bot, game_over
    print(f'На столе: {str(bank)} {candys(bank)}')
    try:
        i = int(input('\nсколько конфет я забираю? Ввести значение: '))
        while i > MAX_TAKE or i < 1:
            i = int(input(f'Напоминаю - диапазон от 1 до {MAX_TAKE}:'))
    except:
        print("Вводите значение правильно!")
        return game_over
    me_have += i
    bank -= i
    if win(bank):
        print('\n\nвсем спасибо, все свободны')
        print(f'{CANDY_CNT} {candys(CANDY_CNT)} - мои!\n\n')
        game_over = 1
    else:
        game_over = 0
    return game_over


def bot_step(power):
    global bot_have, bank, in_bot, game_over, bot_remarks
    time.sleep(0.5)
    print('\nBot: ' + random.choice(bot_remarks) +'\n')
    print(f'На столе: {str(bank)} {candys(bank)}')
    if power == 0:
        i = random.randint(1, MAX_TAKE)
    if power == 1:
        if bank <= MAX_TAKE:
            i = bank
        elif bank % (MAX_TAKE) > 1:
            # внесем элемент случайности в роковую определенность победы AI
            if random.randint(0, 1) and bank % (MAX_TAKE + 1):
                i = bank % (MAX_TAKE + 1) #выигрышный ход - сработает: если предпоследний
            else:
                i = random.randint(1, MAX_TAKE) 
        else:
            i = 1
    if power == 2:
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
        print('\n\nБот: "За AI будущее и все ништяки!"')
        print(f'{CANDY_CNT} {candys(CANDY_CNT)} - мои!\n\n')
        game_over = 1
    else:
        game_over = 0

    return game_over


def play_game(who_start, power):
    global me_have, bot_have, bank, in_bot, game_over
    while not game_over:
        if who_start == 0:
            if my_step():
                break
            if bot_step(power):
                break
        if who_start == 1:
            if bot_step(power):
                break
            if my_step():
                break
        print(
            f'У меня: {me_have} {candys(me_have)}\nУ бота: {bot_have} {candys(bot_have)}')
    game_over = 0


def save(save_mode):
    with open('dialog.json', mode=save_mode, encoding='utf-8') as file:
        file.write(json.dumps(bot_remarks, ensure_ascii=False))


def load(l_file):
    with open(l_file, mode='r', encoding='utf-8') as file:
        lst = json.load(file)
    return lst

        
bot_remarks = load('dialog.json')
help = load('help.json')


who_start = random.randint(0, 1)
power = random.randint(0, 2)
while in_bot:
    print_items(help)
    command = input('\nВаше действие: ')
    if command == '/0':
        who_start = 0
    if command == '/1':
        who_start = 1
    if command == '/2':
        who_start = 1
        power = 2
    if command == '/weak':
        power = 0
    if command == '/middle':
        power = 1
    if command == '/diabolo':
        power = 2
        who_start = 1
    if command == '/power':
        power_choice()
        if command == '/weak':
            power = 0
        if command == '/middle':
            power = 1
        if command == '/diabolo':
            power = 2
            who_start = 1
    if command == '/start':
        print(f"power={power}\nwho_start={who_start}\ngame_over = {game_over}\n")
        play_game(who_start, power)
        game_init()        
    if command == '/stop':
        break
    if command == '/h':
        for item in help:
            print(item)
    else:
        print("Такой вариант не предусмотрен")
        game_init()
