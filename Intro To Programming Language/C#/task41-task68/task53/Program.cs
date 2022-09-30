// Задача 53: Задайте двумерный массив. 
// Напишите программу, 
// которая поменяет местами первую и последнюю строку массива.
int[] OneDimCreateArray(int count, int minVal, int maxVal)
{
    int[] result = new int[count];
    Random ran = new Random();
    for (int i = 0; i < count; i++)
    {
        result[i] = ran.Next(minVal, maxVal + 1);
    }
    return result;
}

void CreateArray(int row, int column, int minVal, int maxVal, out int[,] array)
{
    array = new int[row, column];
    int[] columns; // = new int[column];
    for (int i = 0; i < row; i++)
    {
        columns = OneDimCreateArray(column, minVal, maxVal + 1);
        for (int j = 0; j < column; j++)
        {
            array[i, j] = columns[j];
        }
    }
}


void PrintArray(int[,] array)
{
    Console.WriteLine("[");
    for (int i = 0; i < array.GetLength(0); i++)
    {
        Console.Write("[");
        for (int j = 0; j < array.GetLength(1); j++)
        {
            Console.Write($"{array[i, j]:F2},\t");
        }
        Console.Write("\b\b]\n");
    }
    Console.WriteLine("]");
}

void ConvertArray(int[,] array)
{
    for (int i = 0; i < array.GetLength(1); i++)
    {
        int[] buffer = new int[array.GetLength(1)];
        buffer[i] = array[0, i];
        array[0, i] = array[array.GetLength(0) - 1, i];
        array[array.GetLength(0) - 1, i] = buffer[i];
    }
}

int row = 3;
int column = 5; 
int minVal = -10;
int maxVal = 10;
CreateArray(row, column, minVal, maxVal, out int[,] array);
PrintArray(array);
ConvertArray(array);
PrintArray(array);








