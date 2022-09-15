class Task34
{
    // Задача 34: Задайте массив заполненный случайными положительными трёхзначными числами. 
    // Напишите программу, которая покажет количество чётных чисел в массиве.
    // [345, 897, 568, 234] -> 2
    static int CalcEvenNumbers(int[] arr)
    {
        int cnt = 0;
        foreach (int a in arr)
            if (a % 2 == 0) cnt++;
        return cnt;
    }
    static void RandomFillArray(int[] arr)
    {
        Random ran = new Random();
        for (int i = 0; i < arr.Length; i++)
        {
            arr[i] = ran.Next(100, 1000);
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
        Console.Write($" -> {CalcEvenNumbers(array)} ");
    }
}