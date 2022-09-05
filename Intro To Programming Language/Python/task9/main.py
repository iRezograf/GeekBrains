
#Напишите программу, которая выводит
#случайное число из отрезка [10, 99] и показывает
#наибольшую цифру числа.
#78 -> 8
#12-> 2
#85 -> 8
#Демонстрация решения
#10 99




from decimal import Decimal
from os import write
import random

x = random.randrange(10,99)
xl = x//10
xr = x%10
if (x//10 > x%10):
    print(f"{x} -> {xl}")
else:
    print(f"{x} -> {xr}")
