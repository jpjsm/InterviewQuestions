namespace RotateArrayNxN90DegreesLeft.test;

public class RotateArrayNxNTests
{
    public static IEnumerable<object[]> GetRotateArrayNxN90DegreesLeftTestTestData()
    {
        object[][] testCases = new object[][]{
            new object[]{
                new int[,] { { 0 } },
                new int[,] { { 0 } }
            },
            new object[]{
                new int[,] { { 0, 1 }, { 2, 3 } },
                new int[,] { { 1, 3 }, { 0, 2 } }
            },
            new object[]{
                new int[,] { { 1, 2 , 3 }, { 4, 5, 6 }, { 7, 8, 9 } },
                new int[,] { { 3, 6, 9 }, { 2, 5, 8 }, { 1, 4, 7 } }
            },
            new object[]{
                new int[,] { { 1, 2 , 3, 4 }, { 5, 6, 7, 8 }, { 9, 10, 11, 12 }, { 13, 14, 15, 16 } },
                new int[,] { { 4, 8, 12, 16 }, { 3, 7, 11, 15 }, { 2, 6, 10, 14  }, { 1, 5, 9, 13 } }
            },
        };
        foreach (var testCase in testCases)
        {
            yield return testCase;
        }
    }

    [Theory]
    [MemberData(nameof(GetRotateArrayNxN90DegreesLeftTestTestData))]
    public void RotateArrayNxN90DegreesLeftTest(int[,] given, int[,] expected)
    {
        int[,] actual = RotateArray.RotateArrayNxN90DegreesLeft(given);
        Assert.Equal(expected, actual);
    }
}
