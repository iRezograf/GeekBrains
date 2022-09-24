// Задача 52. Задайте двумерный массив из целых чисел. 
//Найдите среднее арифметическое элементов в каждом столбце.

// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// Среднее арифметическое каждого столбца: 4,6; 5,6; 3,6; 3.


Arrays arrays = new Arrays();
int row = 4;
int column = 5; 
int minVal = -10;
int maxVal = 10;


arrays.CreateArray(row, column, minVal, maxVal, out int [,] array);
arrays.PrintArray(array);


double [] averageByColumns =  arrays.AverageByColumns(array);
Console.Write("// Среднее арифметическое каждого столбца: ");
arrays.PrintArray(averageByColumns);
