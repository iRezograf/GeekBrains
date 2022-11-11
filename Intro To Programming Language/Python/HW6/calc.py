import re

calc_str = '2 * 4 / (-5001+(-1 + 1004 -7 + 4004))'
calc_str = calc_str.replace(" ", '')
print(f'\n\nисходное выражение: {calc_str}')

def expression_in_brackets(expression):
    start = str(expression).rfind('(')
    end = str(expression).find(')')
    return expression, expression[start+1:end]


def calc_in_brackets(full_expression, expression):
    pattern = re.compile(r'([-|+][0-9]+)')
    m = pattern.findall(expression)
    collapsed_exp = ''
    sum = 0
    for i in m:
        sum += int(i)
    collapsed_exp = str(sum)
    full_expression = str(full_expression).replace('('+expression+')', collapsed_exp)
    return full_expression, collapsed_exp


x,y = expression_in_brackets(calc_str)
x,y = calc_in_brackets(x, y)

calc_str = x
x,y = expression_in_brackets(calc_str)
x,y = calc_in_brackets(x, y)

print(x)
print(y)
exit()

while '*' in calc_str or '/' in calc_str:
    if calc_str.find('*') < calc_str.find('/'):
        index = calc_str.find('*')
        # my_str = my_str[:index - 1] + str(int(my_str[index - 1]) * int(my_str[index + 1])) + my_str[index + 2:]
        s1 = calc_str[:index - 1]
        s2 = str(int(calc_str[index - 1]) * int(calc_str[index + 1]))
        s3 = calc_str[index + 2:]
        calc_str = s1 + s2 + s3
    else:
        index = calc_str.find('/')
        calc_str = calc_str[:index - 1] + str(int(calc_str[index - 1]) / int(calc_str[index + 1])) + calc_str[index + 2:]
print(calc_str)