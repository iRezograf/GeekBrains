""" 
Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
*Пример:*
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19 
"""
LOCAL_ROUND = 6

list = [1.1, 1.2, 3.1, 5, 10.01]
sorted_list = []


for f in list:
    right = round(f - int(f), LOCAL_ROUND)
    if right:
        sorted_list.append(right)
sorted_list.sort()
max = sorted_list[len(sorted_list)-1]
min = sorted_list[0]
print(f'{list} => {max-min}') 
