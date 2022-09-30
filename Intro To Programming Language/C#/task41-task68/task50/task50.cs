    Console.WriteLine(
    "// Задача 50. Напишите программу, которая на вход принимает позиции элемента в двумерном массиве,\n" +
    "// и возвращает значение этого элемента или же указание, что такого элемента нет.\n" +
    //"//Например, задан массив:\n" +
    //"//1 4 7 2\n" +
    //"//5 9 2 3\n" +
    //"//8 4 2 4\n" +
    //"//17 -> такого числа в массиве нет"
    "");

    Arrays a = new Arrays();

    int row = new Random().Next(1, 11);
    int column = new Random().Next(1, 11);
    int minValue = -10;
    int maxValue = 10;
    Console.WriteLine($"row = {row}, column = {column}");
    a.CreateArray(row, column, minValue, maxValue, out int[,] array);
    a.PrintArray(array);
    int[] position = a.CreateArrFromKeyboard("введите позиции элемента в формате i,j ");

    if (position[0] < row & position[1] < column)
        Console.WriteLine($"элемент с индексом [{position[0]},{position[1]}] = {array[position[0], position[1]]}");
    else
        Console.WriteLine($"элемента с индексом [{position[0]},{position[1]}] в массиве нет");

