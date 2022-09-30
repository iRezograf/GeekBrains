// Задача 56: Задайте прямоугольный двумерный массив. 
// Напишите программу, которая будет находить строку с наименьшей суммой элементов.


Arrays arrays = new Arrays();
int row = 3;
int column = 5;
int minVal = -10;
int maxVal = 10;

int[][] array = arrays.CreateArray(row, column, minVal, maxVal);
Console.WriteLine("Задан массив:");
arrays.PrintArray(array);

int sum = 0;
int minSum = sum;
for (int j = 0; j < array[0].Length; j++)
{
    sum += array[0][j];
}
minSum = sum;
int rowNumberWithMinSum = 0;
for (int i = 1; i < array.Length; i++)  // для массива массивов array[][] 
                                        // количество строк = array.Length
{
    sum = 0;
    for (int j = 0; j < array[i].Length; j++)
    {
        sum += array[i][j];
    }
    if (sum < minSum)
    {
        minSum = sum;
        rowNumberWithMinSum = i;
    }
}
Console.WriteLine($"Строка с наименьшей суммой {minSum} элементов:\n");
arrays.PrintArray(array[rowNumberWithMinSum]);