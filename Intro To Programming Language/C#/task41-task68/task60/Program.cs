// Задача 60. ...Сформируйте трёхмерный массив из неповторяющихся двузначных чисел. 
// Напишите программу, которая будет построчно выводить массив, 
// добавляя индексы каждого элемента.
// Массив размером 2 x 2 x 2
// 66(0,0,0) 25(0,1,0)
// 34(1,0,0) 41(1,1,0)
// 27(0,0,1) 90(0,1,1)
// 26(1,0,1) 55(1,1,1)


Arrays arrays = new Arrays();
int len = 2;
//int [] lineArray = new int [len*len*len];
int [] lineArray = arrays.CreateArrayUniqValue(2, 10, 99);

int [,,] array = new int [len,len,len];

int pos = 0;
for (int i = 0; i < len; i++)
{
    for (int j = 0; j < len; j++)
    {
        for (int m = 0; m < len; m++)
        {
            array[m,j,i] = lineArray[pos++];
            Console.Write($"{array[m,j,i]} ({m}{j}{i}) ");
        }
        Console.Write($"\n");
        
    }
}
