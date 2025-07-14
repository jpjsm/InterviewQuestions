namespace TypingSuggestion;

public class WordInfo
{
    private string _word = string.Empty;
    private int _position;
    private int _relativeFrequency;

    public string Word => _word;
    public int Position => _position;
    public int RelativeFrequency => _relativeFrequency;

    public WordInfo(string word, int position, int relativeFrequency)
    {
        // validations
        if (string.IsNullOrWhiteSpace(word))
        {
            throw new ArgumentNullException("word");
        }

        if (position < 1)
        {
            throw new ArgumentOutOfRangeException(
                "position",
                position,
                "must be greater than zero ('0')"
            );
        }

        if (relativeFrequency < 1)
        {
            throw new ArgumentOutOfRangeException(
                "relativeFrequency",
                relativeFrequency,
                "must be greater than zero ('0')"
            );
        }

        _word = word;
        _position = position;
        _relativeFrequency = relativeFrequency;
    }

    public override string ToString()
    {
        return $"{_word}, Position: {_position}, Relative Frequency: {_relativeFrequency}";
    }
}
