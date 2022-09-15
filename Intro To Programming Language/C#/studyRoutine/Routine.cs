namespace studyRoutine;
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
}
