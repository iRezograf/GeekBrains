// Задача 62. Напишите программу, которая заполнит спирально массив 4 на 4.
// Например, на выходе получается вот такой массив:
// 01 02 03 04
// 12 13 14 05
// 11 16 15 06
// 10 09 08 07

Arrays arrays = new Arrays();

int[] dimentions = arrays.CreateArrFromKeyboard("введите размер матрицы А в формате: i,j: ");
int[,] array = new int[dimentions[0], dimentions[1]];
int value = 1;
//int CurCol = dimentions[1] - 1;

// отрисовываю первую строку, как частный случай
for (int i = 0; i < dimentions[1]; i++)
    array[0, i] = value++;

// отрисовываю, начиная с правого верхнего угла, общий, рекурсивный случай
value = DrawRect(array, 0, dimentions[1] - 1, dimentions[0], dimentions[1], --value);

arrays.PrintArray(array);


int DrawRect(int[,] array, int curRow, int CurCol, int n, int m, int value)
{
    if (value >= array.GetLength(0) * array.GetLength(1)) return value;

    int bufN = n;
    while (n-- > 0)
        array[curRow++, CurCol] = value++;
    curRow--;
    value--;

    int bufM = m;
    while (m-- > 0)
        array[curRow, CurCol--] = value++;
    CurCol++;
    value--;
    
    // эта проверка нужна только для случая массива из двух строк (2хM)
    if (value >= array.GetLength(0) * array.GetLength(1)) return value;

    n = bufN - 1;
    while (n-- > 0)
        array[curRow--, CurCol] = value++;
    curRow++;
    value--;

    m = bufM - 1;
    while (m-- > 0)
        array[curRow, CurCol++] = value++;
    CurCol--;
    value--;

    n = bufN - 1;
    m = bufM - 1;
    return DrawRect(array, curRow, CurCol, n - 1, m - 1, value);
}


