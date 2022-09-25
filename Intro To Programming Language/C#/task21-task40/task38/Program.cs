// Задача 38: Задайте массив вещественных чисел. 
// Найдите разницу между максимальным и минимальным элементов массива.
// [3 7 22 2 78] -> 76

class Task36
{
    static  void LookUpMaxAndMin(int[] arr, out int max, out int min)
    {
        max = min = arr[0];
        //min = arr[0];
        
        for (int i = 1; i < arr.Length; i++)
            if (arr[i] < min) 
            min = arr[i];
            else if (arr[i] > max)
                max = arr[i];
        //Console.WriteLine($"Max = {max}");
        //Console.WriteLine($"Min = {min}");                        
    }
    static void RandomFillArray(int[] arr)
    {
        Random ran = new Random();
        for (int i = 0; i < arr.Length; i++)
        {
            arr[i] = ran.Next(-10, 10);
        }
    }
    static void PrintArray(int[] arr)
    {
        Console.Write("[");
        foreach (int a in arr)
            Console.Write($"{a}, ");
        Console.Write("\b\b]");
    }
    static void Main(string[] args) // в качестве аргумента передаем длину массива - например: "dotnet run 6"
    {
        //Console.WriteLine("введите длину массива: ");
        //int lenArray;

        bool isInt = int.TryParse(args[0], out int lenArray);
        if (!isInt) { Console.WriteLine(" введено не число..."); return; }

        int[] array = new int[lenArray];

        RandomFillArray(array);
        PrintArray(array);
        LookUpMaxAndMin (array, out int max, out int min);
        Console.WriteLine($" -> {max - min} ");
    }
}