# задача 3.
# Напишите программу, удаляющую из текста все слова,
# содержащие "абв". Функции FIND и COUNT юзать нельзя.


def remove_txt(word, txt):
    result = word
    i = 0
    while i < len(word):
        if word[i:i + len(txt)] == txt:
            return ''
        i += 1
    return result


def search_word(data, txt):
    result = ''
    i = 0
    while i < len(data):
        word = ''
        if data[i].isalpha():
            while data[i].isalpha():
                word += data[i]
                i += 1
            result += remove_txt(word, txt)
            i -= 1
        else:
            result += data[i]
        i += 1
    return result

print('\n'*5)
data = ' абdвначал \nлаопдод\t \ncvcxbb\tадодф,аvбвu абв . дла закончилvпдлабв!'
txt = 'абв'
print('Было :\n"' + data + '"')
print('->')
print('Стало:\n"' + search_word(data, txt) + '"')
