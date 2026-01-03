public static class PermutationsAndCombinations
{
    public static List<T[]> PermutationsWithRepetitions<T>(HashSet<T> s, int size)
    {
        // Convert set to array for consistent access by position
        T[] elements = s.ToArray<T>();

        // Different elements

        int elements_len = elements.Length;

        // Calculate result size
        int result_size = 1;
        for (int i = 0; i < size; i++)
        {
            result_size *= s.Count;
        }

        List<T[]> results = new List<T[]>(result_size);

        for (int i = 0; i < result_size; i++)
        {
            T[] array = new T[size];

            // Make a copy of i to find representation in base 'elements_len'
            int n = i;

            for (int j = 0; j < size; j++)
            {
                array[j] = elements[n % elements_len];
                n /= elements_len;
            }

            results.Add(array);
        }

        return results;
    }

    public static IEnumerable<T[]> PermutationsWithRepetitionsEnumerable<T>(HashSet<T> s, int size)
    {
        // Convert set to array for consistent access by position
        T[] elements = s.ToArray<T>();

        // Different elements

        int elements_len = elements.Length;

        // Calculate result size
        int result_size = 1;
        for (int i = 0; i < size; i++)
        {
            result_size *= s.Count;
        }

        //List<T[]> results = new List<T[]>(result_size);

        for (int i = 0; i < result_size; i++)
        {
            T[] array = new T[size];

            // Make a copy of i to find representation in base 'elements_len'
            int n = i;

            for (int j = 0; j < size; j++)
            {
                array[j] = elements[n % elements_len];
                n /= elements_len;
            }

            yield return array;
        }

        yield break;
    }

    public static T[] FillWith<T>(this T[] array, T value)
    {
        for (int i = 0; i < array.Length; i++)
        {
            array[i] = value;
        }

        return array;
    }
}