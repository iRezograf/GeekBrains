""" 
Задача 4. Напишите программу, 
которая будет преобразовывать десятичное число в двоичное. 
Нельзя использовать готовые функции.
"""

def int_to_binary(b):
    binary_str = ''
    while b:
        binary_str = binary_str + str(b%2)
        b = int(b/2)    
    return  binary_str

i  = 1024
print (f'{i} -> {int_to_binary(i)}')
