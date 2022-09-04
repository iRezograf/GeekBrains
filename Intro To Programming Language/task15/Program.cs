// See https://aka.ms/new-console-template for more information
/*
Задача 15: Напишите программу, которая принимает на вход цифру, 
обозначающую день недели, и проверяет, является ли этот день выходным.

6 -> да
7 -> да
1 -> нет
*/

//string [] namesOfWeekDay = new string[5] {"понедельник", "вторник", "среда","четверг", "пятница"};
Console.Clear();
Console.Write("введите цифру, обозначающую день недели: ");
int i = int.Parse(Console.ReadLine());
if (i > 5)
{
    Console.WriteLine($"{i} -> да");
}
else
{
    Console.WriteLine($"{i} ->  нет");
}