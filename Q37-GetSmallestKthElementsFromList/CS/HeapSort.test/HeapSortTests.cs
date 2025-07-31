namespace jpjsm.SortedHeap.test;

public class HeapSortTests
{
    [Theory]
    [InlineData(1)]
    [InlineData(2)]
    [InlineData(4)]
    [InlineData(8)]
    [InlineData(1024)]
    public void ConstructorTests(int size)
    {
        SortedHeap<int, string> sheap = new SortedHeap<int, string>(size);
        Assert.True(sheap.Empty);
        Assert.Equal(0, sheap.Count);
        Assert.Equal(size, sheap.MaxCapacity);
    }

    [Fact]
    public void ConstructorExceptionTest()
    {
        Assert.Throws<ArgumentOutOfRangeException>(() => new SortedHeap<int, string>(0));
        Assert.Throws<ArgumentOutOfRangeException>(() => new SortedHeap<int, string>(-1));
    }

    [Fact]
    public void PopExceptionTest()
    {
        SortedHeap<int, string> sheap = new SortedHeap<int, string>(10);
        Assert.Throws<ApplicationException>(() => sheap.PopMax());
    }

    [Theory]
    [InlineData(1)]
    [InlineData(2)]
    [InlineData(4)]
    [InlineData(8)]
    [InlineData(1024)]
    public void SingleInsertTests(int size)
    {
        SortedHeap<int, string> sheap = new SortedHeap<int, string>(size);
        sheap.Insert(size, $"{size}");
        Assert.False(sheap.Empty);
        Assert.Equal(1, sheap.Count);
        Assert.Equal(size, sheap.MaxCapacity);
    }

    [Theory]
    [InlineData(1)]
    [InlineData(2)]
    [InlineData(4)]
    [InlineData(8)]
    [InlineData(1024)]
    public void SingleInsertPopTests(int size)
    {
        SortedHeap<int, string> sheap = new SortedHeap<int, string>(size);
        sheap.Insert(size, $"{size}");
        (int key, string data) = sheap.PopMax();
        Assert.Equal(size, key);
        Assert.Equal($"{size}", data);
    }

    [Theory]
    [InlineData(new int[]{1,2})]
    [InlineData(new int[]{1,2,3})]
    [InlineData(new int[]{1,2,3,4})]
    [InlineData(new int[]{1,2,3,4,5})]
    [InlineData(new int[]{1,2,3,4,5,6})]
    [InlineData(new int[]{1,2,3,5,8,13,21,34,55,89})]
    public void MultipleInsertOnePopTests(int[] items)
    {
        SortedHeap<int, string> sheap = new SortedHeap<int, string>(15);
        foreach (int item in items)
        {
            sheap.Insert(item, $"{item}");
        }

        Assert.Equal(items.Length, sheap.Count);
        (int key, string data) = sheap.PopMax();
        int max = items.Max();
        Assert.Equal(max, key);
        Assert.Equal($"{max}", data);
    }

    [Fact]
    public void Fixed100kInsertPopTests()
    {
        int iterations = 100_000;
        SortedHeap<int, string> sheap = new SortedHeap<int, string>(iterations);
        for (int i = 1; i <= iterations; i++)
        {
            sheap.Insert(i, $"{i}");
        }

        Assert.Equal(iterations, sheap.Count);

        for (int i = iterations; i > 0; i--)
        {
            (int actualKey, string actualData) = sheap.PopMax();
            Assert.Equal(i, actualKey);
            Assert.Equal($"{i}", actualData);
        }
    }
}
