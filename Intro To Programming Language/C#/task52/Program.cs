// Задача 52. Задайте двумерный массив из целых чисел. 
//Найдите среднее арифметическое элементов в каждом столбце.

// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3.

double [] AverageByColumns(int [][] array)
{
    double [] result = new double [array[0].Length];
    for (int j = 0; j < array[0].Length; j++)
    {
        double summa = 0;    
        for (int i = 0; i < array.Length; i++)
        {
            summa = summa + array[i][j];
        }
        result[j] = summa/array.Length;
    }
    return result;
}

Arrays arrays = new Arrays();
int row = 3;
int column = 5; 
int minVal = -10;
int maxVal = 10;
int [][] array;
array = arrays.CreateTwoDimensionArray(row, column, minVal, maxVal);
arrays.PrintTwoDimensionArray(array);

double [] averageByColumns =  AverageByColumns(array);

arrays.PrintArray(averageByColumns);

// перегрузка методов
// int [] a = {1,2};
// arrays.PrintArray(a);