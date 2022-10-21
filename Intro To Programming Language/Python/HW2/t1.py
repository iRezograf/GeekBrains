# Задача 1. Напишите программу,
# которая принимает на вход вещественное или целое число и показывает сумму его цифр.
# Через строку нельзя решать.
# *Пример:*
# - 6782 -> 23
# 1. 6782 % 10 = 678 + 2
# 2. 678 % 10 = 67 +   8
# 3. 67 % 10 = 6 +     7
# 4. 6 % 10 = 0 +      6
# 5. 0 % 10 = 0 +      0

# - 0,56 -> 11
# - 12,764 -> 20 


# - 0,764 -> 17 
# 1. 0.764*10 = 7,64 - int(7,64) > 0  
# 


# print(round(7.64 - int(7.64),10))
# print(round(6.4 - int(6.4),10))
# print(round(4 - int(4),10))
# exit()
def to_int(f):
    if f  :
        s = int(f*10)
        #print (f's = {s} дробная часть = {round(f*10 - int(f*10),10)}')
        return s + to_int(round(f*10 - int(f*10),10))
    else:
        return 0

def count_right_f(x):
    if x:
        s = x % 10
        return s + count_right_f(int((x-s)/10))
    else:
        return 0

    

f = 0.764
print(to_int(f))
exit()
#f = float(input('введите вещественное число: '))
right_f = int(f)
left_f = round(f - right_f, 10)
#print (f'right_f = {right_f}  - left_f = {left_f}')

# s=count_right_f(right_f)
print(count_right_f(right_f))
