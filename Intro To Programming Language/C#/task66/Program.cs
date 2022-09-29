using MyStudyLib;
// Задача 66: Задайте значения M и N. 
// Напишите программу, 
// которая найдёт сумму натуральных элементов в промежутке от M до N.

// M = 1; N = 15 -> 120
// M = 4; N = 8. -> 30
Arrays ar = new Arrays();
Console.Clear();
int[] array = ar.CreateArrFromKeyboard("Задайте диапазон для " +
                                    "расчета суммы натуральных элементов от M до N, как M,N ");

Console.WriteLine($"M = {array[0]}; N = {array[1]} -> {ar.SumNElements(array[0], array[1])}");



