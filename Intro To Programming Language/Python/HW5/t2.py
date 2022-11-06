# Реализуйте RLE алгоритм:
# реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
from typing import List, Any


def RLE(data):  # run-length encoding
    # если серия закнчивается в одном буфере, а продолжается в следующем
    # то мой RLE распишет его как два вхождения.
    # это, не нарушает принципа RLE, а процент сжатия становится меньше на велиичину
    # (8/BUFF_SIZE), что пренебрежительно мало для BUFF_SIZE = 4096
    l = []
    if not data:
        return l
    char = data[0]
    cnt = 0
    for item in data:
        if char == item:
            cnt = cnt + 1
        else:
            l.append(str(cnt) + str(char))
            cnt = 1
            char = item
    l.append(str(cnt) + str(char))
    return l


# end def


def convert_txt_to_rle(txt_file_name, rle_file_name):
    f_txt = open(txt_file_name, 'r')
    f_rle = open(rle_file_name, 'w', BUFF_SIZE)
    d_txt = f_txt.read(BUFF_SIZE)
    while d_txt:
        d_rle = RLE(d_txt)
        for item in d_rle:
            f_rle.write(str(item))
        d_txt = f_txt.read(BUFF_SIZE)
    f_rle.close
    f_txt.close


def RLDe(data):  # run-length Decoding
    # data = '33a6s3d1e3q44q3x2y1z3a6s3d1e3q4q3x2y1z'
    # print(data)
    # print ('--------')
    lst = []
    if not data:
        return lst
    i = 0
    while i < len(data) - 1:
        d = data[i]
        digit = ''
        while d.isdigit():
            digit += d
            i = i + 1
            d = data[i]
        # print(digit, end='')
        decoded_str = ''
        for j in range(int(digit)):
            decoded_str += data[i]
        # print(decoded_str)
        i = i + 1
    # for item in lst:
    # print(item)
    return decoded_str




def convert_rle_to_txt(rle_file_name, txt_file_name):
    f_rle = open(rle_file_name, 'r', BUFF_SIZE)
    f_txt = open(txt_file_name, 'w')
    d_rle = f_rle.read(BUFF_SIZE)
    #cut_BUFF_SIZE
    while d_rle:
        d_txt = RLDe(d_rle)
        for item in d_txt:
            f_txt.write(str(item))
        d_rle = f_rle.read(BUFF_SIZE)
    f_rle.close
    f_txt.close


# end def

def print_file(file_name):
    f_txt = open(file_name, 'r', BUFF_SIZE)
    txt = f_txt.read(BUFF_SIZE)
    while txt:
        print(txt, end='')
        txt = f_txt.read(BUFF_SIZE)
    f_txt.close


# end def


# data = 'aaassssssddddddeqqqqqqqxxxyyz'
# f_txt = open('t2.txt', 'w', BUFF_SIZE)
# f_txt.write(data)

BUFF_SIZE = 16  # взял маленькое значение для наглядности
print('\n' * 10)

# convert_txt_to_rle('t2.txt','t2.rle')
# print_file('t2.txt')
# print()
# print_file('t2.rle')

# print()
# data = '33a6s3d1e3q44q3x2y1z3a6s3d1e3q4q3x2y1z'
# RLDe(data)
# print('\n' * 2)

convert_rle_to_txt('t2.rle', 't2.txt')
print_file('t2.rle')
print()
print_file('t2.txt')
