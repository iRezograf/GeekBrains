
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
         '9': 'конфет'}

CANDY_CNT = 51  # по заданию 2021
MAX_TAKE = 12   # по заданию 28
# выиграшная позиция: на столе у противника 28*N +1 конфета
me_have = 0
bot_have = 0
in_bot = 1
in_game = 1
bot_power = {"/000":"тупой", "/333":"не без задатков", "/666":"просто чёрт"}
bank = CANDY_CNT
bot_remarks = []
#bot_remarks =["привет", "до свидания"]


wining_str = 'всем спасибо, все свободны'

def win(cnt):
    if cnt <= 0:
        return True

def bot_power_choice():
    for key, val in bot_power.items():
        print (key, ":", val)

bot_power_choice()
exit()

def my_step():
    i = int(input('сколько конфет я забираю? :'))
    global me_have, bank, in_bot, in_game
    me_have += i
    bank -= i
    if win(bank):
        print('всем спасибо, все свободны')
        print(f'{CANDY_CNT} {candy[str(CANDY_CNT%10)]} - мои!')
        in_bot = 1
        in_game = 0
    return in_game

def bot_step():
    global bot_have, bank, in_bot, in_game, bot_remarks
    time.sleep(0.5)
    print('Bot: ' + random.choice(bot_remarks))

        
    i = random.randint(1, MAX_TAKE)
    print(f'Бот забрал:  {str(i)}  {candy[str(i%10)]}\n')
    bot_have += i
    bank -= i
    if win(bank):
        print('Бот: "За AI будущее и все ништяки!"')
        print(f'{CANDY_CNT} {candy[str(CANDY_CNT%10)]} - мои!')
        in_bot = 1
        in_game = 0
    return in_game

def play_game(who_start):
    global me_have, bot_have, bank, in_bot, in_game
    while in_game:        
        print(f'\nНа столе: {str(bank)} {candy[str(bank%10)]}\n')
        if who_start == 0:
            if not my_step():
                break
            if not bot_step():
                break   
        if who_start == 1:     
            if not bot_step():
                break   
            if not my_step():
                break
        if who_start == 666:     
            if not bot_step():
                break   
            if not my_step():
                break
        print(f'У меня: {me_have} {candy[str(me_have%10)]} У бота: {bot_have} {candy[str(bot_have%10)]}')

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

for item in help:
    print(item)

while in_bot:
    while in_game:
        command = input('ваше действие: ')
        if command == '/0':
            play_game(0)
        if command == '/1':
            play_game(1)
        if command == '/666':
            play_game(666)
        else:
            in_bot = in_game = False
        print(2021 % 28)
        s = input("ваше действие: ")
