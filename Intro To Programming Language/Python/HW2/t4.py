""" Задача 4 НЕОБЯЗАТЕЛЬНАЯ. 
Напишите программу, которая принимает на вход N, 
и координаты двух точек и 
находит расстояние между ними 
в N-мерном пространстве. """


from math import sqrt


with open('Intro To Programming Language/Python/HW2/input_data.txt', 'r',
          encoding="UTF-8") as f:
    lines = []
    for l in f:
        lines.append(l)

n = int(lines[0])   # n - мерное пространство (а ведь еще даже не курили)
p1 = list(map(int, (lines[1].split(','))))
p2 = list(map(int, (lines[2].split(','))))
l = 0
for i in range(n):
    l += (p1[i]-p2[i])**2
l = sqrt(l)  # ** (0.5)


print(n)
print(p1)
print(p2)
print(l)


#d = ((x2 - x1)**2 +(y2 - y1)**2 + (z2 - z1)**2)**(0.5)
