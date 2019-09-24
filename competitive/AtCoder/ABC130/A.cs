using System;
class A
{
    static void Main(string[] args)
    {
        string[] str = Console.ReadLine().Split(' ');
        int x = int.Parse(str[0]);
        int a = int.Parse(str[1]);
        if (x<a){
            System.Console.WriteLine(0);
        }
        else {
            System.Console.WriteLine(10);
        }
    }
}
