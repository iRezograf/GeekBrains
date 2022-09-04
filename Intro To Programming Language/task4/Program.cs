// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");
/*
Задача 4: Напишите программу, которая принимает на вход три числа и выдаёт максимальное из этих чисел.

2, 3, 7 -> 7
44 5 78 -> 78
22 3 9 -> 22
*/

Console.Write("Введите первое число, a ");
int a = int.Parse(Console.ReadLine());
Console.Write("Введите второе число, b ");
int b = int.Parse(Console.ReadLine());
Console.Write("Введите третье число, с ");
int c = int.Parse(Console.ReadLine());

if (a > b && a > c)
{
    Console.Write($"a = {a}, b = {b}, c = {c} -> max = {a} ");
}
else if (b > c)
    {
        Console.Write($"a = {a}, b = {b} -> max = {b} ");
    }
    else 
    {
        Console.Write($"a = {a}, b = {b} -> max = {c} ");
    }
    