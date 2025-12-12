using System;
using System.Data;

namespace MyApp
{
    internal class Program
    {
        public static int GCD(int a, int b)
        {
            if (a <= 0 || b <= 0)
                throw new ArgumentOutOfRangeException("No argument can be less then zero or equal to zero");

            if (a < b)
                (b, a) = (a, b);

            while (b != 0)
                (a, b) = (b, a % b);

            return a;
        }

        public static int LCM(int a, int b)
        {
            return checked( a * (b / GCD(a, b)));
        }
        
        public static int[] CleanArrayToCoprimes(int[] arr1)
        {
            if (arr1.Length < 2)
                return arr1;

            List<int> res = new List<int>();
            res.Add(arr1[0]);
            for (int i = 1; i < arr1.Length; i++)
            {
                if (GCD(arr1[i], res[res.Count - 1]) == 1)
                {
                    res.Add(arr1[i]);
                }
                else
                {
                    int lcm = LCM(arr1[i], res[res.Count - 1]);
                    res[res.Count - 1] = lcm;
                }
            }

            return res.ToArray();
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            int a = short.MaxValue;
            int b = short.MaxValue - 2;
            Console.WriteLine($"a: {a:N0}, b: {b:N0}, GCD: {GCD(a, b):N0} LCM: {LCM(a, b):N0}");
            int[] ints = [6, 4, 3, 30,5, 60, 5, 7];
            Console.WriteLine($"ints: [{string.Join(", ", ints.Select(i => $"{i}"))}], cleaned ints: [{string.Join(", ", CleanArrayToCoprimes(ints).Select(i => $"{i}"))}]");
        }
    }
}