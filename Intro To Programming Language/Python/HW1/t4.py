# Поддерживаемые операции: +, -, /, *,
# mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.


count = 1


def input_params():
    global count
    s = list(input('введите два числа и операцию через пробел: ').split())
    print(f'Sample Input {count}')
    s[0] = float(s[0])
    s[1] = float(s[1])
    print(s[0])
    print(s[1])
    print(s[2])
    return s


s = input_params()
while len(s) != 0:
    if s[2] == '+':
        print(f'Sample Output ', count)
        print(s[0]+s[1])
    elif s[2] == '-':
        print(f'Sample Output ', count)
        print(s[0]-s[1])
    elif s[2] == '*':
        print(f'Sample Output ', count)
        print(s[0]*s[1])
    elif s[2] == '/':
        if (s[1]):
            print(f'Sample Output ', count)
            print(s[0]/s[1])
        else:
            print('Деление на 0!')
    elif s[2] == 'mod':
        print(f'Sample Output ', count)
        print(s[0] % s[1])
    elif s[2] == 'div':
        print(f'Sample Output ', count)
        print(s[0]//s[1])
    elif s[2] == 'pow':
        print(f'Sample Output ', count)
        print(s[0]**s[1])
    count += 1
    s = input_params()
