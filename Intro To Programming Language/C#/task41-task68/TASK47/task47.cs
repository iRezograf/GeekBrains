namespace TASK47
{
    public class task47
    {
        public void main()
        {
            Console.Clear();
            Console.WriteLine(" Задача 47. Задайте двумерный массив размером m×n,\n" +
                                " заполненный случайными вещественными числами.\nПимер:\n" +
                                " m = 3, n = 4.\n\n" +
                                " 0,5 7 -2 -0,2\n" +
                                " 1 -3,3 8 -9,9\n" +
                                " 8 7,8 -7,1 9");
            Arrays a = new Arrays();
            int[] ranksOfArray = a.CreateArrFromKeyboard("введите размерность массива в формате i,j ");
            //double[,] array = new double[ranksOfArray[0], ranksOfArray[1]];
            a.CreateArray(ranksOfArray[0], ranksOfArray[1], -10, 10, out double[,] array);
            a.PrintArray(array);
        }

    }
}