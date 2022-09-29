// Задача 64: Задайте значение N. 
// Напишите программу, которая выведет все чётные числа в промежутке от N до 1. 
// Выполнить с помощью рекурсии.

// N = 5 -> "4, 2"
// N = 8 -> "8, 6, 4, 2"

Console.Write("Задайте значение N: ");
bool isInt = int.TryParse(Console.ReadLine(), out int n);
Console.WriteLine("");

Console.Write($"N = {n} -> \"");
int result = PrintEven(n);
Console.WriteLine("\b\b\"");
int PrintEven(int n)
{
    if (n % 2 == 0) Console.Write($"{n}, ");
    if (n == 2) return 2;
    return PrintEven(n - 1);
}