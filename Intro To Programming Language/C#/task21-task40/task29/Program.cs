// Задача 29: Напишите программу, 
// которая задаёт массив из 8 элементов и выводит их на экран.
// 1, 2, 5, 7, 19 -> [1, 2, 5, 7, 19]
// 6, 1, 33 -> [6, 1, 33]
// Console.WriteLine("Hello, World!");

Console.Clear();
bool isInt = true;
Console.Write($"введите длину массива : ");
isInt = int.TryParse(Console.ReadLine(), out int lenOfArray);
int[] arr = new int[lenOfArray];


isInt = InputArr(arr);
if (isInt)
{
    OutputArr(arr);
}

bool InputArr(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write($"введите {i + 1} -й элемент массива из 8 элементов: ");
        isInt = int.TryParse(Console.ReadLine(), out array[i]);
        if (!isInt)
        {
            Console.WriteLine("Ошибка ввода . . .");
            return isInt;
        }
    }
    return isInt;
}

void OutputArr(int [] array)
{
    Console.Clear();
    foreach (int a in array)
        Console.Write($"{a}, ");
    Console.Write("\b\b -> ["); // \b - удаление последней (лишней) запятой
    foreach (int a in array)
        Console.Write($"{a}, ");
    Console.WriteLine("\b\b]");
}