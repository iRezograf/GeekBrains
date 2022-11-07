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

def search_word(data):



data = ' абвначал \nлаопдод \tcvcxbb \tадодфабвu ++ абв дла закончилvпдлабв'
txt = 'абв'
print(data)
new_data = ""
for word in data.split():
    new_word = remove_txt(word, txt)
    #if new_word:                       # если понадбится удалять лишние пробелы после удаления слов
    #    new_data += new_word + " "     # если понадбится удалять лишние пробелы после удаления слов
    new_data += new_word + "+"
#new_data = new_data.rstrip()           # если понадбится удалять лишние пробелы после удаления слов
new_data = new_data[:-1] #
print('"' + new_data + '"')
