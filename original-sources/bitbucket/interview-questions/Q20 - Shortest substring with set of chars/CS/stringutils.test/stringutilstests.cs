namespace stringutils.test;

public class StringUtilsTests
{
    [Theory]
    [InlineData("abracadabra","", "")]
    [InlineData("abracadabra","123", "")]
    [InlineData("abracadabra","abc", "brac")]
    [InlineData("aaaaaaaaaabbbbbbbbbbcccccccccc","abc", "abbbbbbbbbbc")]
    public void ShortestSubstringContainingTests(string txt, string chars, string expected)
    {
        HashSet<char> charsset = [.. chars];
        string actual = txt.ShortestSubstringContaining(charsset);
        Assert.Equal(expected, actual);
    }
}
