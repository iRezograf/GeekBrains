using System;
namespace TASK49
{
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

        public void PrintArray(int[][] array)
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

        public void PrintArray(int[,] array)
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

        public void PrintArray(double [,] array)
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
                result[j] = summa / array.GetLength(1);
            }
            return result;
        }

    }
}