// Задача 58: Задайте две матрицы. Напишите программу, 
// которая будет находить произведение двух матриц.
// Например, даны 2 матрицы:
// 2 4 | 3 4
// 3 2 | 3 3
// Результирующая матрица будет:
// 18 20
// 15 18



Arrays arrays = new Arrays();
int minVal = 2;
int maxVal = 4;

int[] dimA = arrays.CreateArrFromKeyboard("введите размер матрицы А в формате: i,j: ");
int[] dimB = arrays.CreateArrFromKeyboard("введите размер матрицы B в формате: i,j: ");

Console.WriteLine($"Заданы матрицы :");

arrays.CreateArray(dimA[0], dimA[1], minVal, maxVal, out int[,] arrayA);
arrays.PrintArray(arrayA);

Console.WriteLine("");
arrays.CreateArray(dimB[0], dimB[1], minVal, maxVal, out int[,] arrayB);
arrays.PrintArray(arrayB);
if (dimA[1] == dimB[0])
{
    arrays.MatrixMultiplicate(arrayA, arrayB, out int[,] arrayM);
    arrays.PrintArray(arrayM);
}
else
    Console.WriteLine("Число столбцов первой матрицы не равно числу строк второй матрицы.\n" +
    "Умножать матрицы нельзя ");
