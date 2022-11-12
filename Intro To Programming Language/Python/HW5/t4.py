# задача 4
# x_необязательная_ Даны два многочлена. Задача - сформировать их сумму.
# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9
import re


def get_structure(multinom):
    # multinom - член у многочлена
    if not len(multinom):
        return {}
    znak = 1
    ratio = 0  # коэффициент
    power = 0  # степень
    if multinom[0] == '-':
        znak = -1
        multinom = multinom[1:]
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
        else:
            ratio = 1
    return {power: znak * ratio}


def f_sort(val):
    if val.find(':') != -1:
        ratio = int(val[:val.find(':')])
    else:
        ratio = int(val)
    return ratio


def deparsing(item):
    # power: ratio
    m = item.split(':')
    power = m[0]
    ratio = m[1]
    #print(f'{power}:{ratio}')
    if ratio > '0':
        ratio = "+"+ratio
    if ratio == '0':
        return ' '
    if power == '0':
        return f'{ratio}'
    if power == '1':
        return f'{ratio}*x'
    if ratio == '+1' and power > '1':
        return f'x^{power}'
    if ratio == '-1' and power > '1':
        return f'-x^{power}'
    else:
        return f'{ratio}*x^{power}'


str1 = '5 * x ^ 22 - x^4 - 2*x^2 + 5*x - 6'
str2 = '-3*x^22 + 5*x^10 -3*x^3 -  8*x + 3'

list_m1 = str1.replace(' ', '')
list_m2 = str2.replace(' ', '')

list_m1 = list_m1.replace('+', '.+')
list_m1 = list_m1.replace('-', '.-')

list_m2 = list_m2.replace('+', '.+')
list_m2 = list_m2.replace('-', '.-')

list_m1 = list_m1.split('.')
list_m2 = list_m2.split('.')

m1_structure = {}
m2_structure = {}
for item in list_m1:
    m1_structure.update(get_structure(item))
for item in list_m2:
    m2_structure.update(get_structure(item))

m_structure = []
for m1 in m1_structure:
    val = 0
    if m1 in m2_structure:
        val = m2_structure.pop(m1)
    m_structure.append(f'{m1}:{int(m1_structure[m1]) + int(val)}')  # сложение коэффициентов
for m2 in m2_structure:
    m_structure.append(f'{m2}:{m2_structure[m2]}')

m_structure.sort(reverse=True, key=f_sort)

sum_m1_m2 = ''
for i in m_structure:
    sum_m1_m2 = sum_m1_m2 + deparsing(i)
if sum_m1_m2[0] == "+":
    sum_m1_m2=sum_m1_m2[1:]

print(str1)
print(str2)
print('сумма многочленов:')
print(sum_m1_m2)
