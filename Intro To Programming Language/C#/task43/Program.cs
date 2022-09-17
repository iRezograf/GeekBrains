
// Задача 43: Напишите программу, 
// которая найдёт точку пересечения двух прямых, 
// заданных уравнениями y = k1 * x + b1, y = k2 * x + b2; 
// значения b1, k1, b2 и k2 задаются пользователем.
// b1 = 2, k1 = 5, b2 = 4, k2 = 9 -> (-0,5; -0,5)

double [] Point(double [][] arr)
{
    double [] res = new double [2];
    res[0] = (arr[1][1] - arr[0][1]) / (arr[0][0] - arr[1][0]);
    res[1] = arr[0][0] * res[0] + arr[0][1];
    return res;
}

MyClasses mc = new MyClasses();
double[][] arr = new double[2][];
string prompt;

prompt = "введите параметры 1-й линии (y = k * x + b) в формате k, b: ";
arr[0] = mc.CreateArrFromKeyboard(prompt);
prompt = "введите параметры 2-й линии (y = k * x + b) в формате k, b: ";
arr[1] = mc.CreateArrFromKeyboard(prompt);

if (arr[0][0] == arr[1][0])
    Console.WriteLine("прямые не пересекаются ...");
else
{
    double [] point = Point(arr);
    
    Console.Write($"b1 = {arr[0][1]}, ");
    Console.Write($"k1 = {arr[0][0]}, ");
    Console.Write($"b2 = {arr[1][1]}, ");
    Console.Write($"k2 = {arr[1][0]} -> ");
    Console.Write($"( x = {point[0]}, ");
    Console.WriteLine($" y = {point[1]} )");
}
