// Задача 51: Задайте двумерный массив. 
//Найдите сумму элементов, находящихся на главной диагонали 
//(с индексами (0,0); (1;1) и т.д.
// Например, задан массив:
// 1 4 7 2
// 5 9 2 3
// 8 4 2 4
// Сумма элементов главной диагонали: 1+9+2 = 12

Console.Write("Введите количество строк массива: ");
int rows = int.Parse(Console.ReadLine());

Console.Write("Введите количество столбцов массива: ");
int columns = int.Parse(Console.ReadLine());

int minValue = 0;
int maxValue = 10;

int[,] array = GetArray(rows, columns, minValue, maxValue);
PrintArray(array);
Console.WriteLine("");
Console.WriteLine($"Сумма диагональных чисел = {SumElementsOfDiagonal(array)}");

int[,] GetArray(int m, int n, int minValue, int maxValue)
{
    int[,] result = new int[m, n];
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            result[i, j] = new Random().Next(minValue, maxValue + 1);
        }
    }
    return result;
}

void PrintArray(int[,] inArray)
{
    for (int i = 0; i < inArray.GetLength(0); i++)
    {
        for (int j = 0; j < inArray.GetLength(1) ; j++)
        {
            Console.Write($"{inArray[i,j]} ");
        }
        Console.WriteLine();
    }
    
}

int SumElementsOfDiagonal(int [,] array)
{
    int result = 0;
    // считаем только для значений диагонали, игнорируя остальной массив
    // каким бы большим он ни был
    int lenDiagonal = (array.GetLength(0) < array.GetLength(1)? 
                                            array.GetLength(0): 
                                            array.GetLength(1));                                        
    for (int i = 0; i < lenDiagonal; i++)
    {
        result = result +array [i,i]; 
    }
    return result;
}
