namespace TypingSuggestion;

class Program
{
    public const int LongestPrefix = 4;

    static void Main(string[] args)
    {
        Dictionary<string, int>[] frequencies = new Dictionary<string, int>[LongestPrefix + 1];
        for (int i = 1; i < LongestPrefix + 1; i++)
        {
            frequencies[i] = new Dictionary<string, int>();
        }

        WordsList commonwords = new WordsList("../English-most-common-words.csv");
        foreach (WordInfo w in commonwords)
        {
            for (int i = 0; i < LongestPrefix; i++)
            {
                if (i >= w.Word.Length)
                {
                    break;
                }

                if (!frequencies[i + 1].ContainsKey(w.Word.Substring(0, i + 1)))
                {
                    frequencies[i + 1].Add(w.Word.Substring(0, i + 1), 0);
                }

                frequencies[i + 1][w.Word.Substring(0, i + 1)] += 1;
            }
        }

        for (int i = 1; i < LongestPrefix + 1; i++)
        {
            foreach (string k in frequencies[i].Keys.OrderBy(k => k))
            {
                Console.WriteLine($"{k:5}: {frequencies[i][k]}");
            }

            Console.WriteLine();
            Console.WriteLine("---------------------");
            Console.WriteLine();
        }
    }
}
