public static class PermutationsAndCombinations
{
    public static List<T[]> PermutationsWithRepetitions<T>(HashSet<T> s, int size)
    {
        int len = 1;
        for (int i = 0; i < size; i++)
        {
            len *= s.Count;
        }

        T[] elements = s.ToArray<T>();
        List<T[]> results = new List<T[]>(len);

        for (int i = 0; i < len; i++)
        {
            T[] array = new T[size];

            int n = i;
            for (int j = 0; j < size; j++)
            {
                array[j] = elements[n % elements.Count()];
                n /= elements.Count();
            }

            results.Add(array);
        }

        return results;
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