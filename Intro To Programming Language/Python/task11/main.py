# Решение в группах задач:
# 11. Напишите программу, которая выводит случайное
# трёхзначное число и удаляет вторую цифру этого
# числа. 

# 456 -> 46
# 782 -> 72
# 918 -> 98
# 12 мин

from ast import Str
import random
import cut


s = str(random.randrange(100,999))
print(f"{s} -> {cut.cuting(s,1,1)}")
