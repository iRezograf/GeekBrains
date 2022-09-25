// Задача 19
// Напишите программу, которая принимает на вход пятизначное число и проверяет, является ли оно палиндромом.
// 14212 -> нет
// 12821 -> да
// 23432 -> да

Console.Clear();
int origRow = Console.CursorTop;
int origCol = Console.CursorLeft;

int lenOfPolindrom = 4;

Console.SetCursorPosition(origCol, origRow);
Console.Write($"введите {lenOfPolindrom}-значное число:");

int number;
string strNumber = Console.ReadLine();
bool success = int.TryParse(strNumber, out number);
while (lenOfPolindrom != strNumber.Length || !success)
{
    Console.Beep();
    Console.Clear();
    Console.SetCursorPosition(origCol, origRow);
    Console.Write($"введите {lenOfPolindrom}-значное число:");;
    strNumber = Console.ReadLine();
    success = int.TryParse(strNumber, out number);
}

bool isPolindrom = true;
for (int i = 0; i < strNumber.Length/2; i++)
{
    if (strNumber[i] != strNumber[strNumber.Length - 1 - i]) 
    {
        isPolindrom = false;
        break;        
    }   

}
if (isPolindrom)    
    Console.WriteLine($"{strNumber} -> да");
else                
    Console.WriteLine($"{strNumber} -> нет");
