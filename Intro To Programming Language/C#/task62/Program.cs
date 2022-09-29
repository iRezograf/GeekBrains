// Задача 62. Напишите программу, которая заполнит спирально массив 4 на 4.
// Например, на выходе получается вот такой массив:
// 01 02 03 04
// 12 13 14 05
// 11 16 15 06
// 10 09 08 07

Arrays arrays = new Arrays();

Console.WriteLine(4534%10);


int[] dimentions = arrays.CreateArrFromKeyboard("введите размер матрицы А в формате: i,j: ");
int[,] array = new int[dimentions[0], dimentions[1]];

for (int i = 0; i < dimentions[0]; i++)
{
    for (int j = 0; j < dimentions[1]; j++)
    {
        array[i, j] = i * dimentions[1] + j;
        array[i, j] = 0;
        //Console.WriteLine(array[i, j].ToString("00.00"));
    }
}

array[0,0] = 0;
Right(array, 0, 0, dimentions[1]-1);
arrays.PrintArray(array);


void Right(int [,] array, int positionRow, int positionColumn, int countHope)
{
    for (int i = 1; i <= countHope; i++)
    {
        array[positionRow,positionColumn+i] = array[positionRow,positionColumn]+1;
        Console.Write(array[positionRow,positionColumn+i]+ "");
        //positionRow++;
        //positionColumn++;
    }
}
/* void UpRight(int [,] array, int i, int j, int count)
{
    
}

void DownLeft(int [,] array, int positionRow, int positionColumn, int countHope, int value)
{
    for (int i = 1; i <= countHope; i++)
    {
        array[positionRow,positionColumn+i] = array[positionRow,positionColumn]+1;
    }
} */