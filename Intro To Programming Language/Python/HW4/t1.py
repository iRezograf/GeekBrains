# задача 1. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

import random


n = random.randint(0,99)
smpl_multipliers = []
i = n
while i: 
    if not n%i:
        smpl_multipliers.append(i)
    i -= 1
    
# (sic) ...которая составит список простых множителей числа N.
# но не выводит :-)   
#for i in smpl_multipliers:
#    print(i)