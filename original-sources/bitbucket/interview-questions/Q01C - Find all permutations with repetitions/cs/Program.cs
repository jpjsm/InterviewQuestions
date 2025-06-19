// See https://aka.ms/new-console-template for more information
List<char[]> permutations = PermutationsAndCombinations.PermutationsWithRepetitions(new HashSet<char>(){'!', '@', '#', '$'}, 3);
foreach (char[] array in permutations)
{
    for (int i = 0; i < array.Length; i++)
    {
        Console.Write($"{array[i]} ");
    }

    Console.WriteLine();
}
