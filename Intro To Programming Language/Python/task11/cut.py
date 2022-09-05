
# При необходимости мы можем получить из строки не только отдельные символы, но и подстроку. 
# Для этого используется следующий синтаксис:
# string[:end]: извлекается последовательность символов начиная с 0-го индекса по индекс end (не включая)
# string[start:end]: извлекается последовательность символов начиная с индекса start по индекс end (не включая)


import string

# This function cut 
# from string "s" 
# "count" symbols 
# is begun from "start" position
# and return any symbols  
def  cuting(s, start, count):
    return s[:start] + s[(start + count) :]
    