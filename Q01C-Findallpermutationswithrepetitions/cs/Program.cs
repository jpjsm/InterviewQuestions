namespace test_findpermutationswithrepetitions;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hello, World!");
        int n = 0;

        // List<char[]> permutations = PermutationsAndCombinations.PermutationsWithRepetitions(new HashSet<char>() { '!', '@', '#', '$' }, 3);
        // foreach (char[] array in permutations)
        // {
        //     Console.Write($"{n,4:N0}: ");
        //     for (int i = 0; i < array.Length; i++)
        //     {
        //         Console.Write($"{array[i]} ");
        //     }

        //     Console.WriteLine();
        //     n += 1;
        // }

        n = 0;
        foreach (char[] array in PermutationsAndCombinations.PermutationsWithRepetitionsEnumerable(new HashSet<char>() { '!', '@', '#', '$' }, 3))
        {
            Console.Write($"{n,4:N0}: ");
            for (int i = 0; i < array.Length; i++)
            {
                Console.Write($"{array[i]} ");
            }

            Console.WriteLine();
            n += 1;
        }
    }
}
