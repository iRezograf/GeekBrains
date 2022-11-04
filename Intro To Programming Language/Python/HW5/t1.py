
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
candy = {'0':'конфет',
         '1':'конфета',
         '2':'конфеты',
         '3':'конфеты',
         '4':'конфеты',
         '5':'конфет',
         '6':'конфет',
         '7':'конфет',
         '8':'конфет',
         '9':'конфет'}


in_game = 1
in_bot = 1
CANDY_CNT = 51
MAX_TAKE = 12

runing_str = 'всем спасибо, все свободны'
def runing_string(runing_str):
    for i in runing_str:
        for pos in range(80,0,-1):
            print(f'{i:^pos} ',end='')
    #print(f'{CANDY_CNT} {candy[str(CANDY_CNT%10)]} - мои!')

runing_string(runing_str)
exit()

def win(cnt):
    if cnt <= 0:
        return True
    
def play_game():
    bank = CANDY_CNT
    me_have = 0
    bot_have = 0
    while in_game:
        print(f'\nНа столе: {str(bank)} {candy[str(bank%10)]}\n')
        i = int(input('сколько конфет я забираю? :'))
        me_have += i
        bank -= i
        if win(bank):
            print('всем спасибо, все свободны')
            print(f'{CANDY_CNT} {candy[str(CANDY_CNT%10)]} - мои!')
            
            in_bot =1
            break
            
        time.sleep(1)
        print('Bot: ' + random.choice(bot_remarks))
        time.sleep(2)
        i = random.randint(1, MAX_TAKE)
        
        #print('Bot забрал: ' + str(i) + ' конфет')
        print(f'Bot забрал:  {str(i)}  {candy[str(i%10)]}\n')
        bank -= i
        if win(bank):
            print('Bot: за AI будущее и все ништяки!')
            print(f'{CANDY_CNT} {candy[str(CANDY_CNT%10)]} - мои!')
            
            in_bot =1
            break
        bot_have += i
        print(f'У меня: {me_have} {candy[str(me_have%10)]}\t\tУ бота: {bot_have} {candy[str(bot_have%10)]}')


bot_remarks = []
#bot_remarks =["привет", "до свидания"]


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
play_game()
exit()
while in_bot:
    while in_game:
        command = input('ваше действие: ')
        if command == '/start':
            play_game()
        else:
            in_bot = in_game = False
        print(2021 % 28)
        s = input("ваше действие: ")
