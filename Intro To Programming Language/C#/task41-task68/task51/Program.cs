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

int minValue = -10;
int maxValue = 10;

Arrays a = new Arrays();
a.CreateArray(rows, columns, minValue, maxValue, out int[,] array);
a.PrintArray(array);
Console.WriteLine("");
SumElementsOfDiagonal(array, out string arrayAsString, out int summaElements);
Console.WriteLine($"Сумма элементов главной диагонали: {arrayAsString}  = {summaElements}");





void SumElementsOfDiagonal(int[,] array, out string arrayAsString, out int summaElements)
{
    int[] diagonalArray = ElementsOfDiagonal(array);
    summaElements = diagonalArray[0];
    arrayAsString = diagonalArray[0].ToString();
    for (int i = 1; i < diagonalArray.Length; i++)
    {
        summaElements = summaElements + diagonalArray[i];
        arrayAsString = String.Join(" + ", arrayAsString, diagonalArray[i].ToString());
    }

}

int[] ElementsOfDiagonal(int[,] array)
{
    int lenDiagonal = (array.GetLength(0) < array.GetLength(1) ?
                                            array.GetLength(0) :
                                            array.GetLength(1));
    // цикл сокращаем до размера дианонали
    int[] result = new int[lenDiagonal];
    for (int i = 0; i < lenDiagonal; i++)
    {
        // в виде массива возвращаем только диагональ
        result[i] = array[i, i];
    }
    return result;
}
