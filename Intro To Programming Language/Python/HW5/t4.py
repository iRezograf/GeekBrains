# задача 4
# x_необязательная_ Даны два многочлена. Задача - сформировать их сумму.
# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9
import re


def get_structure(multinom):
    # multinom - член у многочлена
    ratio = 0  # коэффициент
    power = 0  # степень
    if multinom.find('^') == -1 and multinom.find('*') == -1:
        ratio = int(multinom)
        power = 0
    if multinom.find('^') == -1 and multinom.find('*') != -1:
        ratio = int(multinom[:multinom.find('*')])
        power = 1
    if multinom.find('^') != -1:
        power = int(multinom[multinom.find('^') + 1:])
        if multinom.find('*') != -1:
            ratio = int(multinom[:multinom.find('*')])
    return {power: ratio}


def f_sort(val):
    if val.find(':') != -1:
        ratio = int(val[:val.find(':')])
    else:
        ratio = int(val)
    return ratio


m1 = '5 * x ^ 22 + x^4 + 2*x^2 + 5*x + 6'
m2 = '7*x^22 + 5*x^10+ 3*x^3 +  8*x + 3'

list_m1 = m1.replace(' ', '').split('+')
list_m2 = m2.replace(' ', '').split('+')
list_m1 = m1.replace(' ', '').split('+')
list_m2 = m2.replace(' ', '').split('+')
# print(list_m1)
# print(list_m2)

m1_structure = {}
m2_structure = {}
for item in list_m1:
    m1_structure.update(get_structure(item))

for item in list_m2:
    m2_structure.update(get_structure(item))
# print(m1_structure)
# print(m2_structure)

list = []
for m1 in m1_structure:
    val = 0

    if m1 in m2_structure:
        val = m2_structure.pop(m1)
        # print(f'{m1}:{m1_structure[m1]}:{val}')
    list.append(f'{m1}:{m1_structure[m1]}:{val}')
for m2 in m2_structure:
    list.append(f'{m2}:{m2_structure[m2]}')

list.sort(reverse=True, key=f_sort)
for i in list:
    print(i)
print('depars')
for item in list:
    m = item.split(':')
    ratio = 0
    #print(m)
    for i in range(1,len(m)):
        #print(m[i])
        ratio += int(m[i])
        if ratio == 0:
            print('')
        if ratio == 1:
            print(f'x^{m[0]}')
        else:
            print(f'{ratio}*x^{m[0]}')
    print('--------')


# print(m1_structure)
# print(m2_structure)

# thisdict.update({"color": "red"})


# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
