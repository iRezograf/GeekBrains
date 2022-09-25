// Задача 54: Задайте двумерный массив. Напишите программу, 
// которая упорядочит по убыванию элементы каждой строки двумерного массива.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// В итоге получается вот такой массив:
// 7 4 2 1
// 9 5 3 2
// 8 4 4 2
//

Arrays arrays = new Arrays();
int row = 5;
int column = 5;
int minVal = -10;
int maxVal = 10;

int[][] array = arrays.CreateArray(row, column, minVal, maxVal);
Console.WriteLine("Задан массив:");
arrays.PrintArray(array);

Console.WriteLine("В итоге получается вот такой массив:");
foreach (int[] arr in array)
{
    Console.WriteLine("");
    arrays.InsertionSort(arr);
    arrays.PrintArray(arr);
}
