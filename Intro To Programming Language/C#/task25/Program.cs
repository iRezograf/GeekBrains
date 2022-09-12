// Задача 25: Напишите цикл, который принимает на вход два числа (A и B) 
// и возводит число A в натуральную степень B.
// 3, 5 -> 243 (3⁵)
// 2, 4 -> 16

Console.Clear();
/*
int a = InputNum("введите А: ");
int b = InputNum("введите B: ");
Console.WriteLine($"{a}, {b} -> {Math.Pow(a, b)}");


int InputNum(string str)
{
    Console.WriteLine(str);
    bool isInteger = int.TryParse(Console.ReadLine(), out int result);
    if (!isInteger)
    {
        Console.WriteLine("введено не число! ... ");
    }
    return result;
}
*/

// Здесь нет вызова функций, зато правильно обрабатывается ввод "не числа"
string alarm = "введено не число! ...";
Console.WriteLine("введите А: ");
bool isInteger = int.TryParse(Console.ReadLine(), out int c);
if (isInteger)
{
    Console.WriteLine("введите B: ");
    isInteger = int.TryParse(Console.ReadLine(), out int d);
    if (isInteger)
    {
        Console.WriteLine($"{c}, {d} -> {Math.Pow(c, d)}");
    }
    else
    {
        Console.WriteLine(alarm);
    }
}
else
{
    Console.WriteLine(alarm);
}