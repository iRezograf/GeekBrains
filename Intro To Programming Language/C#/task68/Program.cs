using MyStudyLib;
// Задача 68: Напишите программу вычисления функции 
// Аккермана с помощью рекурсии. 
// Даны два неотрицательных числа m и n.
// m = 2, n = 3 -> A(m,n) = 9
// m = 3, n = 2 -> A(m,n) = 29
Arrays ar = new Arrays();
Console.Clear();
int[] array = ar.CreateArrFromKeyboard("Задайте числа для " +
                                    "для вычисления функции Аккермана в формате  m,n: ");
Console.WriteLine($"m = {array[0]}; n = {array[1]} -> A(m,n) = {ar.Akkerman(array[0], array[1])}");
