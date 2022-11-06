# задача 3. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# управляющая послдовательность, позволяет отображать только вторую
# и третью степень с использованием chr(0x00b2) и chr(0x00b3)
# степень придется прописать через **

from random import randint


def blok(n, nn):
    if n == nn == 1:
        return 'x'
    elif n == 1:
        return str(nn) + '*x'
    elif nn == 0:
        return ''
    elif n == 0:
        return str(nn)
    else:
        return str(nn) + '*x**'+str(n)


k = randint(1, 2)
data = ''

kk = randint(0, 2)
if kk != 0:
    if k == 1:
        if kk == 1:
            data = 'x' + ' '
        else:
            data = str(kk) + '*x' + ' '
    else:
        if kk == 1:
            data = data + 'x**'+str(k) + ' '
        else:
            data = data + str(kk) + '*x**'+str(k) + ' '

k -= 1

while k:
    kk = randint(0, 2)
    if kk != 0:
        if k == 1:
            if kk == 1:
                data = data + '+ ' + 'x' + ' '
            else:
                data = data + '+ ' + str(kk) + '*x' + ' '
        else:
            if kk == 1:
                data = data + '+ ' + 'x**'+str(k) + ' '
            else:
                data = data + '+ ' + str(kk) + '*x**'+str(k) + ' '
    k -= 1

data = data + '+ ' + str(randint(1, 101)) + ' = 0'

with open('./temp.txt', 'w', encoding="UTF-8") as file:
    file.write(data)

with open('./temp.txt', 'r', encoding="UTF-8") as file:
    d = file.read()
print(d)
