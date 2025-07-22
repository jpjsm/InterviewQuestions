namespace RemoveDuplicatesFromLinkedList.test;

public class LinkedListTests
{
    [Fact]
    public void DefaultLinkedLIstIsNull()
    {
        LinkedList list = new LinkedList();
        Assert.Null(list.Head);
    }

    [Fact]
    public void ListWithOneItem()
    {
        LinkedList list = new LinkedList();
        list.Insert('A');
        IEnumerable<char> expected = ['A'];
        Assert.Equal(expected, list.Scan());
    }


    [Fact]
    public void ListWithTwoItems()
    {
        LinkedList list = new LinkedList();
        list.Insert('A');
        list.Insert('B');
        IEnumerable<char> expected = ['B', 'A'];
        Assert.Equal(expected, list.Scan());
    }


    [Fact]
    public void ListWithManyItems()
    {
        char[] data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'];

        LinkedList list = new LinkedList();
        foreach (char letter in data)
        {
            list.Insert(letter);
        }

        IEnumerable<char> expected = data.Reverse();
        Assert.Equal(expected, list.Scan());
    }

    [Theory]
    [InlineData(new object[] { new char[] { 'A'}, new char[] { 'A' } })]
    [InlineData(new object[] { new char[] { 'A', 'B'}, new char[] { 'B', 'A' } })]
    [InlineData(new object[] { new char[] { 'A', 'B', 'C'}, new char[] { 'C', 'B', 'A' } })]
    [InlineData(new object[] { new char[] { 'A', 'B', 'C', 'D'}, new char[] { 'D', 'C', 'B', 'A' } })]
    [InlineData(new object[] { new char[] { 'A', 'B', 'C', 'D', 'E'}, new char[] { 'E', 'D', 'C', 'B', 'A' } })]
    [InlineData(new object[] { new char[] { 'A', 'B', 'C', 'D', 'E', 'F'}, new char[] { 'F', 'E', 'D', 'C', 'B', 'A' } })]
    [InlineData(new object[] { new char[] { 'A', 'B', 'C', 'D', 'E', 'F', 'G'}, new char[] { 'G', 'F', 'E', 'D', 'C', 'B', 'A' } })]
    [InlineData(new object[] { new char[] { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H' }, new char[] { 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A' } })]
    [InlineData(new object[] { new char[] { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I' }, new char[] { 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A' } })]
    [InlineData(new object[] { new char[] { 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J' }, new char[] { 'J', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A' } })]
    [InlineData(new object[] { new char[] { 'A', 'A' }, new char[] { 'A' } })]
    [InlineData(new object[] { new char[] { 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A' }, new char[] { 'A' } })]
    [InlineData(new object[] { new char[] { 'A', 'A', 'B', 'C', 'A', 'A', 'B', 'C','A', 'A', 'B', 'C','A', 'A', 'B', 'C','A', 'A', 'B', 'C'}, new char[] { 'C', 'B', 'A' } })]

    public void RemoveDuplicates(char[] data, char[] expectedArray)
    {
        LinkedList list = new LinkedList();
        foreach (char letter in data)
        {
            list.Insert(letter);
        }

        IEnumerable<char>? expected = expectedArray;
        list.RemoveDuplicates();
        IEnumerable<char>? actual = list.Scan();
        Assert.Equal(expected, actual);
    }
}
