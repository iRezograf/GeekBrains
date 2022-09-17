public class MyClasses
{
    public int [] CreateArray(int count, int minVal, int maxVal)
    {
        int [] result = new int [count];
        Random ran = new Random();
        for (int i = 0; i < count; i++)
        {
            result[i] = ran.Next(minVal, maxVal);
        }
        return result;
    }

    public void PrintArray(int[] arr)
    {
        Console.Write("[");
        foreach (int a in arr)
            Console.Write($"{a}, ");
        Console.Write("\b\b] ");
    }
}