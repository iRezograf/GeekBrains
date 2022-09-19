import string


def Fill_Figure(array, old_Character, new_Character, hight, wight):
    if (array[hight][wight] == old_Character):
        array[hight][wight] = new_Character
        # for i in array:
        #     print()
        #     for j in i:
        #         print(j, end=" ")
        # a = input ("press any key in method ...")
        Fill_Figure(array, old_Character, new_Character, hight-1, wight)
        Fill_Figure(array, old_Character, new_Character, hight, wight-1)
        Fill_Figure(array, old_Character, new_Character, hight+1, wight)
        Fill_Figure(array, old_Character, new_Character, hight, wight+1)

    # for i in array:
    #    print (i)
    #a = input ("press any key in method ...")
    # array [10, 10] = "*"
