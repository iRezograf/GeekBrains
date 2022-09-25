// See https://aka.ms/new-console-template for more information

// 16. Напишите программу, которая принимает на вход два числа и проверяет, 
//является ли одно число квадратом другого.
// 5, 25  ->  да
// -4, 16  ->  да
// 25, 5  ->  да
// 8,9  ->  нет

Console.Write("Введите первое число, a ");
int a = int.Parse(Console.ReadLine());
Console.Write("Введите второе число, b ");
int b = int.Parse(Console.ReadLine());


if (a*a == b | b*b == a)
{
    Console.Write($"a = {a}, b = {b}, ->  да");
}
else 
{
    Console.Write($"a = {a}, b = {b}, ->  нет");
}

    