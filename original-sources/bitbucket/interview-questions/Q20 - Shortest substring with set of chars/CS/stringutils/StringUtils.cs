namespace stringutils;

public static class StringUtils
{
    public static string ShortestSubstringContaining(this string txt, HashSet<char> chars)
    {
        bool hasSolution = false;
        int left = 0;
        int right = txt.Length - 1;
        int minlen = right - left + 1;
        bool foundAll = false;
        int substringlen = txt.Length - 1;
        for (int i = 0; i < txt.Length - chars.Count+1; i++)
        {
            HashSet<char> charsFound = new HashSet<char>();
            substringlen = txt.Length - 1;
            for (int j = i; j < txt.Length; j++)
            {
                if (chars.Contains(txt[j]))
                {
                    charsFound.Add(txt[j]);
                    foundAll = chars.Intersect(charsFound).Count() == chars.Count;
                    substringlen = j - i + 1;
                }

                if (foundAll)
                {
                    hasSolution = true;
                    if (substringlen == chars.Count) return txt.Substring(i, substringlen);
                    if (substringlen < minlen)
                    {
                        minlen = substringlen;
                        left = i;
                        right = j;
                    }
                    break;
                }
            }
        }

        if (!hasSolution) return string.Empty;
        return txt.Substring(left, right - left + 1);
    }
}
