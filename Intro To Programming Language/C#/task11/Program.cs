// See https://aka.ms/new-console-template for more information
/*
11. Напишите программу, которая выводит случайное трёхзначное число и удаляет вторую цифру этого числа.
456 -> 46
782 -> 72
918 -> 98
*/
int a = new Random().Next(100,1000);
int f = a/100;
int m = a/10;
//Console.WriteLine(m);
int l = a - (m*10);
//Console.WriteLine(l);
Console.Write($"{a} -> {f}{l} ");
