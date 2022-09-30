public class Arrays
{
    public double[] CreateArray(int count, int minVal, int maxVal)
    {
        double[] result = new double[count];
        Random ran = new Random();
        for (int i = 0; i < count; i++)
        {
            result[i] = ran.Next(minVal, maxVal);
        }
        return result;
    }

    public void PrintArray(double[] arr)
    {
        Console.Write("[");
        foreach (double a in arr)
            Console.Write($"{a}, ");
        Console.Write("\b\b] ");
    }

    public double [] CreateArrFromKeyboard(string prompt)
    {
        Console.Clear();
        Console.Write(prompt);
        string str = Console.ReadLine();
        string[] strArray = str.Split(',');
        int len = strArray.Length;
        double[] arr = new double[len];

        if (len != 0)
        {
            int i = 0;
            foreach (string item in strArray)
            {
                bool isInt = double.TryParse(item, out double res);
                if (isInt)
                {
                    arr[i] = res;
                    i++;
                }
                else
                {
                    Console.WriteLine("введено не число ...");
                    double [] notInt = new double[0];
                    return notInt;
                }
            }
        }
        return arr;
    }
}