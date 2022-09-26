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

    public void CreateArray(int count, int minVal, int maxVal, out int[] array)
    {
        array = new int[count];
        Random ran = new Random();
        for (int i = 0; i < count; i++)
        {
            array[i] = ran.Next(minVal, maxVal + 1);
        }
    }

    public int[][] CreateArray(int row, int column, int minVal, int maxVal)
    {
        int[][] result = new int[row][];
        for (int i = 0; i < row; i++)
        {
            result[i] = CreateArray(column, minVal, maxVal + 1);
        }
        return result;
    }

    public void CreateArray(int row, int column, int minVal, int maxVal, out int[,] array)
    {
        array = new int[row, column];
        int[] columns; // = new int[column];
        for (int i = 0; i < row; i++)
        {
            columns = CreateArray(column, minVal, maxVal + 1);
            for (int j = 0; j < column; j++)
            {
                array[i, j] = columns[j];
            }
        }
    }

    public void PrintArray(int[] arr)
    {
        Console.Write("[");
        foreach (int a in arr)
            Console.Write($"{a,8:F0}, ");
        Console.Write($"\b\b] ");
    }

    public void PrintArray(double[] arr)
    {
        Console.Write("[");
        foreach (double a in arr)
            Console.Write($"{a,8:F2}, ");
        Console.Write($"\b\b] ");
    }

    public void PrintArray(int[][] array)
    {
        Console.WriteLine("[");
        foreach (int[] row in array)
        {
            Console.Write("[");
            foreach (int e in row)
            {
                Console.Write($"{e,8:F0}, ");
            }
            Console.Write("\b\b]\n");
        }
        Console.WriteLine("]");
    }

    public void PrintArray(int[,] array)
    {
        Console.WriteLine("[");
        for (int i = 0; i < array.GetLength(0); i++)
        {
            Console.Write("[");
            for (int j = 0; j < array.GetLength(1); j++)
            {
                Console.Write($"{array[i, j],8:F0}, ");
            }
            Console.Write("\b\b]\n");
        }
        Console.WriteLine("]");
    }

    public void PrintArray(double[,] array)
    {
        Console.WriteLine("[");
        for (int i = 0; i < array.GetLength(0); i++)
        {
            Console.Write("[");
            for (int j = 0; j < array.GetLength(1); j++)
            {
                Console.Write($"{array[i, j],8:F2}, ");
            }
            Console.Write("\b\b]\n");
        }
        Console.WriteLine("]");
    }

    public int[] CreateArrFromKeyboard()
    {
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

    public int[] CreateArrFromKeyboard(string prompt)
    {
        Console.Write(prompt);
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
    public double[] AverageByColumns(int[][] array)
    {
        double[] result = new double[array[0].Length];
        for (int j = 0; j < array[0].Length; j++)
        {
            double summa = 0;
            for (int i = 0; i < array.Length; i++)
            {
                summa = summa + array[i][j];
            }
            result[j] = summa / array.Length;
        }
        return result;
    }

    public double[] AverageByColumns(int[,] array)
    {
        double[] result = new double[array.GetLength(1)];
        for (int j = 0; j < array.GetLength(1); j++)
        {
            double summa = 0;
            for (int i = 0; i < array.GetLength(0); i++)
            {
                summa = summa + array[i, j];
            }
            result[j] = summa / array.GetLength(0);
        }
        return result;
    }

    public void InsertionSort(int[] array)
    {
        int key;
        int i;
        for (int j = 1; j < array.Length; j++)
        {
            key = array[j];
            i = j - 1;
            while (i >= 0 && array[i] < key)
            {
                array[i + 1] = array[i];
                i = i - 1;
            }
            array[i + 1] = key;
        }
    }
    public void MatrixMultiplicate(int[,] aMatrix, int[,] bMatrix, out int[,] product)
    // https://learn.microsoft.com/ru-ru/cpp/parallel/amp/walkthrough-matrix-multiplication?
    // view=msvc-160&viewFallbackFrom=vs-2019
    // проверка работы программы: 
    // https://ru.onlinemschool.com/math/assistance/matrix/multiply/?
    // oms_all=a%3d%7b%7b4,5%7d,%7b2,2%7d,%7b4,5%7d%7d,b%3d%7b%7b3,4,5,2%7d,%7b4,2,3,3%7d%7d
    {
        product = new int[aMatrix.GetLength(0),bMatrix.GetLength(1)];
        for (int row = 0; row < aMatrix.GetLength(0); row++)
        {
            for (int col = 0; col < bMatrix.GetLength(1); col++)
            {
                for (int inner = 0; inner < bMatrix.GetLength(0); inner++)
                {
                    product[row,col] += aMatrix[row,inner] * bMatrix[inner,col];
                }
            }
        }
    }
}
