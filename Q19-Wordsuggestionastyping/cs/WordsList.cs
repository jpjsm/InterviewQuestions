using System.Collections;

namespace TypingSuggestion;

public class WordsList : IEnumerable<WordInfo>
{
    private List<WordInfo> _words = new List<WordInfo>();

    public int Count => _words.Count;

    public WordInfo this[int index]
    {
        get => _words[index];
        set => _words[index] = value;
    }

    public WordsList()
    {
        // Do nothing, explicit default constructor
    }

    public WordsList(FileInfo words)
    {
        if (words == null)
        {
            throw new ArgumentNullException("words");
        }

        if (!words.Exists)
        {
            throw new FileNotFoundException(null, words.FullName);
        }

        using (StreamReader txt = words.OpenText())
        {
            string? line;
            while ((line = txt.ReadLine()) != null)
            {
                if (line.StartsWith("Word,Position,RelativeWeight"))
                {
                    continue;
                }

                string[] elements = line.Split(',');
                string word = elements[0].ToLowerInvariant().Trim();
                int position = int.Parse(elements[1]);
                int relativeFrequency = int.Parse(elements[2]);
                _words.Add(new WordInfo(word, position, relativeFrequency));
            }
        }
    }

    public WordsList(string filename) : this(new FileInfo(filename)) { }

    public IEnumerator<WordInfo> GetEnumerator()
    {
        foreach (WordInfo wordInfo in _words)
        {
            yield return wordInfo;
        }
    }

    IEnumerator IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
    }
}
