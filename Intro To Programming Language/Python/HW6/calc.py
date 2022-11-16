import re


def expression_in_brackets(expression):
    # выделяет блоки от открывающей до закрывающей круглой скобки
    # вложенные в том числе
    pattern = re.compile(r"\([^(^)]+\)")
    m = pattern.findall(expression)
    x = expression
    while m != []:
        for i in m:
            # print(f'i: {i}->',end='')
            x = calc_in_brackets(x, i)
        m = pattern.findall(x)
    return x


def calc_in_brackets(full_expression, expression):
    pattern = re.compile(r"[-|+]*[\.0-9]+")
    m = pattern.findall(expression)
    sum = 0
    for i in m:
        sum += float(i)
    # print(sum)
    full_expression = str(full_expression).replace(expression, str(sum))
    return full_expression


def multiplicate(full_expression):
    pattern = re.compile(r"[\.0-9]+\*[\.0-9]+")  # не работает для вещественных чисел
    m = pattern.findall(full_expression)
    while m != []:
        for i in m:
            pos = str(i).find('*')
            # print("pos:"+str(i)[:pos])
            # print("pos:"+str(i)[pos+1:])
            value = float(str(i)[:pos]) * float(str(i)[pos + 1:])
        full_expression = str(full_expression).replace(i, str(value))
        m = pattern.findall(full_expression)
    # print(full_expression)
    return full_expression


def divide(full_expression):
    pattern = re.compile(r"[\.0-9]+\/[\.0-9]+")
    m = pattern.findall(full_expression)
    while m != []:
        for i in m:
            pos = str(i).find('/')
            if (str(i)[pos + 1:]) != '0':
                value = float(str(i)[:pos]) / float(str(i)[pos + 1:])
            else:
                return 'NaN'
                # print('деление на ноль недопустимо!')
        full_expression = str(full_expression).replace(i, str(value))
        m = pattern.findall(full_expression)
    # print(full_expression)
    return full_expression


def plus_minus(full_expression):
    pattern = re.compile(r"[-|+]*[\.0-9]+")
    m = pattern.findall(full_expression)
    sum = float(0)
    for i in m:
        sum += float(i)
        full_expression = str(sum)
    return full_expression


def percentage(full_expression):
    pattern = re.compile(r"[-+]?[\.0-9]+%?")
    m = pattern.findall(full_expression)
    sum = float(0)
    if m:
        sum = float(str(m[0]))
        for i in range(1, len(m)):
            if str(m[i]).find('%') > 0:
                if i != 0:
                    f = float(str(m[i]).rstrip('%'))
                    p = float(m[i - 1])
                    sum += p * f / 100
                    return str(sum)
                else:
                    print('неотчего брать процент')
                    return 'NaN'
            sum += float(str(m[i]))
    else:
        ret = 'NaN'


def calc_expression(expression) -> str:
    expression = expression.replace(" ", '')
    expression = expression.replace(",", '.')
    expression = multiplicate(expression)
    expression = divide(expression)
    expression = expression_in_brackets(expression)
    expression = multiplicate(expression)
    expression = divide(expression)
    expression = plus_minus(expression)
    return expression


def prepare_expression(expression):
    full_expression = expression.replace(" ", '')
    full_expression = full_expression.replace(",", '.')
    ''' проверка, три pyака подряд - ошибка '''
    pattern = re.compile(r"[-+*\/]{3,}")
    m = pattern.findall(full_expression)
    if m:
        return 'NaN'
    ''' конец проверки '''
    return full_expression


def brackets(full_expression):
    pattern = re.compile(r"\([-+ *\/.\d\s]+\)")
    m = pattern.search(full_expression)
    if not m:
        full_expression = calculate(full_expression)
        return full_expression

    while m:
        s = calculate(full_expression[m.start():m.end()])
        full_expression = full_expression[:m.start()] + s + full_expression[m.end():]
        # cprint(full_expression)
        m = pattern.search(full_expression)
    return full_expression


def calculate(full_expression):
    m = re.search(r'[-+ *\ /][*\ /]', full_expression)
    if m:
        print('Недопустимая компбинация операций')
        return 'NaN'
    full_expression = full_expression.replace(")", '')
    full_expression = full_expression.replace("(", '')

    # pattern = 'r[-+]?[0-9.]+[*\/][-+]?[0-9.]+'
    m = re.search(r"[-+]?[0-9.]+[*\/][-+]?[0-9.]+", full_expression)
    # деление
    while m:
        mm = re.search(r'/', m[0])
        print(f'mm= {mm}')
        if mm:
            d = full_expression[m.start():m.end()]
            if (d[mm.end():]) != '0':
                value = float(d[:mm.start()]) / float(d[mm.end():])
                full_expression = full_expression[:m.start()] + "+" + str(value) + full_expression[m.end():]
                print(full_expression)
            else:
                print('ошибка = деление на ноль')
                return 'NaN'

        m = re.search(r"[-+]?[0-9.]+[*\/][-+]?[0-9.]+", full_expression)
        print(m)
        # умножение
        if m:
            mm = re.search(r'\*', m[0])
        if mm:
            d = full_expression[m.start():m.end()]
            print(d)
            value = float(d[:mm.start()]) * float(d[mm.end():])
            full_expression = full_expression[:m.start()] + "+" + str(value) + full_expression[m.end():]
        m = re.search(r"[-+]?[0-9.]+[*\/][-+]?[0-9.]+", full_expression)
        if not m:
            break
    return full_expression


expression = '(49+ (200 *- 25/(5+7)*12))'
# expression = '(49+ (200 *- 25*4,5/5)'
expression = '1*5-122*23+4.0/-2'
# print(re.search(r"[-+]?[0-9.]+[*\/][-+]?[0-9.]+", expression))
# exit()
print(f'expression : {expression}')
expression = prepare_expression(expression)
print(brackets(expression))
exit()

# print('percentage:'+ percentage('150+0.5%'))
# demo
print(calc_expression(' 5--5'))
