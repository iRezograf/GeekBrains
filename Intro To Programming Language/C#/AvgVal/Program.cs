// Найти среднее по величине значение

int[] arr = { 13, 28, 5, 23, 12, 33, 14 };
Console.Clear();
Console.WriteLine("Имеем массив:");
foreach (int e in arr)
    Console.Write($"{e} ");

double avgVal = 0;
foreach (int e in arr)
    avgVal = avgVal + e;
int len = arr.Length;
avgVal = avgVal / len;
//Console.Write($"\nСреднее значение: ");
Console.WriteLine(avgVal);

double nearVal = avgVal - arr[0];
int posOfAvgVal = 0;
for (int i = 1; i < len; i++)
{
    if (Math.Abs(avgVal - arr[i]) < nearVal)
    {
        posOfAvgVal = i;
        nearVal = Math.Abs(avgVal - arr[i]);
    }
}
Console.WriteLine($"\nСреднее значание в массиве -> {arr[posOfAvgVal]}");
