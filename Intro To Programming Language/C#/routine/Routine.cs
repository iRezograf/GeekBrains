namespace routine;
public class Routine

{
    static void PrintArray(int[] arr)
    {
        Console.Write("[");
        foreach (int a in arr)
            Console.Write($"{a}, ");
        Console.Write("\b\b]");
    }

    static void FillArray(int[] arr)
    {
        Random ran = new Random();
        for (int i = 0; i < arr.Length; i++)
        {
            arr[i] = ran.Next(100, 1000);
        }
    }
    static void Main(string[] args) // в качестве аргумента передаем длину массива - например: "dotnet run 6"
    {
        //Console.WriteLine("введите длину массива: ");
        //int lenArray;

        bool isInt = int.TryParse(args[0], out int lenArray);
        if (!isInt) { Console.WriteLine(" введено не число..."); return; }
        //int lenArray = int.Parse(args[0]);

        int[] array = new int[lenArray];

        FillArray(array);
        PrintArray(array);
        //Console.Write($" -> {CalcEvenNumbers(array)} ");
    }
}
