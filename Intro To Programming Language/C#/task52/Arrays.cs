public class Arrays
{
    public int[] CreateArray(int count, int minVal, int maxVal)
    {
        int[] result = new int[count];
        Random ran = new Random();
        for (int i = 0; i < count; i++)
        {
            result[i] = ran.Next(minVal, maxVal + 1);
        }
        return result;
    }


    public int[][] CreateTwoDimensionArray(int row, int column, int minVal, int maxVal)
    {
        int[][] result = new int[row][];
        for (int i = 0; i < row; i++)
        {
            result[i] = CreateArray(column, minVal, maxVal + 1);
        }
        return result;
    }

    public void PrintArray(int[] arr)
    {
        Console.Write("[");
        foreach (int a in arr)
            Console.Write($"{a}, ");
        Console.Write($"\b\b] ");
    }
    
    public void PrintArray(double[] arr)
    {
        Console.Write("[");
        foreach (double a in arr)
            Console.Write($"{a:F2}, ");
        Console.Write($"\b\b] ");
    }
    public void PrintTwoDimensionArray(int[][] array)
    {
        Console.WriteLine("[");
        foreach (int[] row in array)
        {
            Console.Write("[");
            foreach (int e in row)
            {
                Console.Write($"{e}, ");
            }
            Console.Write("\b\b]\n");
        }
        Console.WriteLine("]");
    }

    public int[] CreateArrFromKeyboard()
    {
        Console.Clear();
        Console.Write($"введите  массив в формате x1, x2,... : ");
        string str = Console.ReadLine();
        string[] strArray = str.Split(',');
        int len = strArray.Length;
        int[] arr = new int[len];

        if (len != 0)
        {
            int i = 0;
            foreach (string item in strArray)
            {
                bool isInt = Int32.TryParse(item, out int res);
                if (isInt)
                {
                    arr[i] = res;
                    i++;
                }
                else
                {
                    Console.WriteLine("введено не число ...");
                    int[] notInt = new int[0];
                    return notInt;
                }
            }
        }
        return arr;
    }
}