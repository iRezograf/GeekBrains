""" 
Задача 4. Напишите программу, 
которая будет преобразовывать десятичное число в двоичное. 
Нельзя использовать готовые функции.
"""

def int_to_binary(i):
    binary_str = ''
    b=i
    for j in range(16):
        binary_str = binary_str + str(b%2)
        b = int(b/2)
    return  binary_str

i  = 2**15 + 2
print (int_to_binary(i))