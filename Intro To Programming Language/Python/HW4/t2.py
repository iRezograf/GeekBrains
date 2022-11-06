# задача 2 . Задайте последовательность чисел.
# Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint


def found_unic(list, item):
    lst = []
    for i in list:
        lst.append(i)

    if (item in lst):
        lst.remove(item)
        if (item in lst):
            #print (f'{item}<-найдено 2-й раз, значит, не уникальное')
            return False
        else:
            return True

#    создание тестовой последовательности
n = 6       # длина    последовательности
list = []   # заданная последовательность
unic_list = []
while n:
    list.append(randint(0, 20))
    n -= 1
print(f'заданная     последовательность: \n{list}')

for i in list:
    if found_unic(list, i):
        unic_list.append(i)
print(f'\'уникальная\' последловательность: \n{unic_list}')
