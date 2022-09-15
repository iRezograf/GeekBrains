// Задача 36: Задайте одномерный массив, заполненный случайными числами. 
// Найдите сумму элементов, стоящих на нечётных позициях.
// [3, 7, 23, 12] -> 19
// [-4, -6, 89, 6] -> 0

class Task36
{
    static int SumEvenNumbers(int[] arr)
    {
        int sum = 0;
        for (int i = 1; i < arr.Length; i += 2)
            sum = sum + arr[i];
        return sum;
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
        Console.WriteLine($" -> {SumEvenNumbers(array)} ");
    }
}