my_str = '2 * 4 / 5'
my_str = my_str.replace(" ", '')

while '*' in my_str or '/' in my_str:
    if my_str.find('*') < my_str.find('/'):
        index = my_str.find('*')
        # my_str = my_str[:index - 1] + str(int(my_str[index - 1]) * int(my_str[index + 1])) + my_str[index + 2:]
        s1 = my_str[:index - 1]
        s2 = str(int(my_str[index - 1]) * int(my_str[index + 1]))
        s3 = my_str[index + 2:]
        my_str = s1 + s2 + s3
    else:
        index = my_str.find('/')
        my_str = my_str[:index-1] + str(int(my_str[index-1]) / int(my_str[index+1])) + my_str[index + 2:]
print(my_str)