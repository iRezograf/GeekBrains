""" 
Задача 5 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. 
проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z . 
Но теперь количество предикатов не три, 
а генерируется случайным образом от 5 до 25, проверяем это утверждение 100 раз, 
с помощью модуля time выводим на экран , сколько времени отработала программа. 
"""

from random import randint

list =[]
predicats = []
for j in range(100):
    predicat_count = randint(5,26)
    list.clear()
    predicats.clear()
    left_statement = 0
    right_statement = not 0
    for i in range(1,predicat_count,1):
        predicats.append(i)
        left_statement = left_statement or i
        right_statement = right_statement and not i
        
    left_statement = not left_statement 
    print(f'{j} predicat_count = {predicat_count}\
        верно ли: {left_statement == right_statement}')