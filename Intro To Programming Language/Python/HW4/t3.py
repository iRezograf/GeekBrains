# задача 3. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# управляющая послдовательность, позволяет отображать только вторую
# и третью степень с использованием chr(0x00b2) и chr(0x00b3)
# степень придется прописать через **

from random import randint


def block(n, nn):
    if n == nn == 1:
        return 'x'
    elif n != 0 and nn == 1:
        return 'x**'+str(n)
    elif nn == 0:
        return ''
    elif n == nn == 0:
        return ''
    elif n == 0:
        return str(nn)
    elif n == 1:
        return str(nn) + '*x'
    else:
        return str(nn) + '*x**'+str(n)


k = randint(1, 3)
data = []


for k in range(3, -1, -1):
    kk = randint(0, 12)
    data.append(block(k, kk))
    #print(f'kk = {kk}, k = {k}, -> {block(k, kk)}')
    k -= 1
for item in data:
    print(item)
d = "+".join(data)
print(d)
exit()


with open('./temp.txt', 'w', encoding="UTF-8") as file:
    file.write(data)

with open('./temp.txt', 'r', encoding="UTF-8") as file:
    d = file.read()
print(d)
