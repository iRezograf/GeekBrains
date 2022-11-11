# Реализуйте RLE алгоритм:
# реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
from typing import List, Any


def RLE(data):  # run-length encoding
    result = ''
    if not data:
        return result
    char = data[0]
    cnt = 0
    for item in data:
        if char == item:
            cnt = cnt + 1
        else:
            result += str(cnt) + str(char)
            cnt = 1
            char = item
    result += str(cnt) + str(char)
    return result

def RLDe(data):  # run-length Decoding
    lst = []
    if not data:
        return lst
    i = 0
    decoded_str = ''
    while i < len(data) - 1:
        d = data[i]
        digit = ''
        while d.isdigit():
            digit += d
            i = i + 1
            d = data[i]
        for j in range(int(digit)):
            decoded_str += data[i]
        i = i + 1
    return decoded_str
def convert_txt_to_rle(txt_file_name, rle_file_name):
    f_txt = open(txt_file_name, 'r')
    f_rle = open(rle_file_name, 'w')
    d_txt = f_txt.read()
    d_rle = RLE(d_txt)
    f_rle.write(d_rle)
    f_rle.close
    f_txt.close

def convert_rle_to_txt(rle_file_name, txt_file_name):
    f_rle = open(rle_file_name, 'r')
    f_txt = open(txt_file_name, 'w')
    d_rle = f_rle.read()
    f_txt.write(RLDe(d_rle))
    f_rle.close
    f_txt.close

def print_file(file_name):
    f_txt = open(file_name, 'r')
    txt = f_txt.read()
    while txt:
        print(txt)
        txt = f_txt.read()
    f_txt.close

# data = 'aaassssssddddddeqqqqqqqxxxyyz'
# f_txt = open('t2.txt', 'w')
# f_txt.write(data)

print('\n' * 10)

print('конвертация текста в RLE')
print_file('t2.txt')
convert_txt_to_rle('t2.txt','t2.rle')
print_file('t2.rle')
print()

# print()
# data = '33a6s3d1e3q44q11x2y11z'
# RLDe(data)
# print('\n' * 2)

print('конвертация RLE в текст')
print_file('t2.rle')
convert_rle_to_txt('t2.rle', 't2.txt')
print_file('t2.txt')
