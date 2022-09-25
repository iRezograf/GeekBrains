// Задача 27: Напишите программу, 
//которая принимает на вход число и выдаёт сумму цифр в числе.
// 452 -> 11
// 82 -> 10
// 9012 -> 12

Console.Clear();
Console.Write("введите число: ");
bool isInt = double.TryParse(Console.ReadLine(), out double x);
if (isInt)
{
    Console.Write($"{x} -> ");
    double s = 0;
    x = SumNum(x, out s) % 10 + s;
    Console.WriteLine(x);

    double SumNum(double x, out double s)
    {
        //Console.WriteLine($"цифра: {x % 10}");
        double a = x % 10;
        if (x > 10)
        {

            x = SumNum((x - x % 10) / 10, out s);
            s = s + a;
            //Console.WriteLine($"\t сумма: {s}");
            return x;
        }
        s = 0;
        return x;
    }
}
else
{
    Console.WriteLine("Ошибка ввода ...");
}