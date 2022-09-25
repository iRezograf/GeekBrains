// Задача 21
// Напишите программу, которая принимает на вход 
//координаты двух точек и находит расстояние между ними в 3D пространстве.
// A (3,6,8); B (2,1,-7), -> 15.84
// A (7,-5, 0); B (1,-1,9) -> 11.53
//  sqrt( pow((x1-x2),2) + pow((y1-y2),2) + pow((z1-z2),2) )

int origRow = Console.CursorTop;
int origCol = Console.CursorLeft;

int[,] points = new int[2, 3];
/*
points[0,0] = 3;
points[0,1] = 6;
points[0,2] = 8;
points[1,0] = 2;
points[1,1] = 1;
points[1,2] = -7;
double res = 15.842;
*/

//for (int i = 1; i <= 2; i++)
//{
//    InputPoint("введите " + i + "-е значение в формате (x,y,z): ", points, i - 1);
//}

InputPoint("введите координаты точки А формате (x,y,z): ", points, 0); // 0 элемент массива points[0,i]
InputPoint("введите координаты точки B формате (x,y,z): ", points, 1); // 1 элемент массива points[0,i]

Console.Write($"A ({points[0,0]},{points[0,1]},{points[0,2]}); ");
Console.Write($"B ({points[1,0]},{points[1,1]},{points[1,2]}) -> ");
//Console.WriteLine($"{lengthBetween(points):F2}");
Console.WriteLine( "{0,0:F2}",LengthBetween(points) );

double LengthBetween(int[,] pnt)
{
    double result = 0;
        for (int j = 0; j <  3; j++)

        {
            result = result + Math.Pow((pnt[0,j] - pnt[1,j]),2);
        }
    return Math.Sqrt(result);
}


void InputPoint(string prompt, int[,] point, int currentPoint)
{
    string alarm = "координты введены в неверном формате \n\t Press any key ...";
    bool isRight = true;
    Console.Beep();
    Console.Clear();
    Console.Write($"{prompt}");
    string strNumber = Console.ReadLine();
    string[] coordinates = strNumber.Split(',');

    if (coordinates.Length != 3)
    {
        Console.WriteLine(alarm);
        Console.ReadLine();
    }
    for (int i = 0; i < 3; i++)
    {
        if (int.TryParse(coordinates[i], out var n))
        {
            point[currentPoint, i] = n;
        }
        else
            Console.Write(alarm);
            Console.ReadLine();
    }
}

