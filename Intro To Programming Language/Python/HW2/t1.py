# Задача 1. Напишите программу,
# которая принимает на вход вещественное или целое число и показывает сумму его цифр.
# Через строку нельзя решать.
# *Пример:*
# - 6782 -> 23
# алгоритм рекурсии для левой части
# 1. 6782 % 10 = 678 + 2
# 2. 678 % 10 = 67 +   8
# 3. 67 % 10 = 6 +     7
# 4. 6 % 10 = 0 +      6
# 5. 0 % 10 = 0 +      0
#
# алгоритм рекурсии для правой части
# - 0,764 -> 17
# 1. 0.764*10 = 7,64 - int(7,64) > 0
#
# print(round(7.64 - int(7.64),10))
# print(round(6.4 - int(6.4),10))
# print(round(4 - int(4),10))
# exit()
LOCAL_ROUND = 6


def count_right(f):
    if f:
        s = int(f*10)
        return s + count_right(round(f*10 - int(f*10), LOCAL_ROUND))
    else:
        return 0


def count_left(x):
    if x:
        s = x % 10
        return s + count_left(int((x-s)/10))
    else:
        return 0


f = float(input('введите вещественное число\nне более 6 знаков после точки: '))
left = int(f)
right = round(f - left, LOCAL_ROUND)


print(f'{f} -> {count_left(left) + count_right(right)}')
