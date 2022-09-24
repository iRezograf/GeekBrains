using System;
namespace TASK49
{
    public class task49
    {
        public void PowToTwoEvenElementsOfArray(int [,] array)
        {
            for (int i = 0; i < array.GetLength(0); i++)
            {
                for (int j = 0; j < array.GetLength(1); j++)
                {
                    if (i % 2 == 0 & j % 2 == 0)
                        array[i, j] = array[i, j] * array[i, j];
                }
            }
        }

        public void PowToTwoEvenElementsOfArray()
        {
            Console.WriteLine("//Задача 49: Задайте двумерный массив.\n" +
                                "//Найдите элементы, у которых оба индекса чётные,\n" +
                                "//и замените эти элементы на их квадраты.\n"
                                );
            Arrays a = new Arrays();
            int row = 3;
            int column = 4;
            int minValue = -10;
            int maxValue = 10;
            a.CreateArray(row,column,minValue,maxValue,out int[,] array);
            a.PrintArray(array);
            PowToTwoEvenElementsOfArray(array);
            a.PrintArray(array);
        }
    }
}

