// Напишите программу, которая принимает на вход число (N) 
// и выдаёт таблицу кубов чисел от 1 до N.
// 3 -> 1, 8, 27
// 5 -> 1, 8, 27, 64, 125

Console.Clear();
Console.Write("введите число N: ");
bool isInt = int.TryParse(Console.ReadLine(), out int n);
int isNegative = n < 0 ? -1: 1;


if (!isInt)
{
    Console.Clear();
    Console.WriteLine("вы ввели не число ... \n Press any key ...");
    Console.ReadLine();
}
else
{
    Console.Write($"{n} -> ");
    for (int i = 1; i < n * isNegative; i++)
    {
        Console.Write($"{Math.Pow(i * isNegative,3)}, ");
    }
    Console.WriteLine($"{Math.Pow(n,3)}");
}    