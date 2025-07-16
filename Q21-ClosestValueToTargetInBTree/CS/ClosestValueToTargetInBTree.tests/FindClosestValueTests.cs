namespace FindClosestValue.tests;
/*

Given a binary tree find the closest value to target.

Example:

               |
              31
            /    \
          17      61
         /  \     /  \ 
        7    29  47   89
         \   /       /  \
         13 23     71    97

if target =  31 ; return 31
if target =   5 ; return  7
if target = 106 ; return 97
if target =  30 ; return 31 or 29
if target =  26 ; return 23 or 29

*/

public class FindClosestValueTests:IDisposable
{
    private Node root;
    public Node Root => root;

    public FindClosestValueTests()
    {
        int[] values = [31, 17, 61, 7, 29, 47, 89, 13, 23, 71, 97];
        root = new Node(values[0]);
        for (int i = 1; i < values.Length; i++)
        {
            root.Insert(values[i]);            
        }
    }


    public void Dispose()
    {
    }

    [Theory]
    [InlineData(36,31, null)]
    [InlineData(24,23, null)]
    [InlineData(6,7, null)]
    [InlineData(98,97, null)]
    [InlineData(30,29, 31)]
    [InlineData(26,23, 29)]
    [InlineData(14,13, null)]
    [InlineData(15,13, 17)]
    [InlineData(16,17, null)]
    public void FindClosestToTargetIterativeTest( int target, int expected, int? alternate)
    {
        int actual = Node.FindClosestValueIterative(target, Root);
        if (alternate.HasValue)
        {
            int[] possibleValues = [expected, alternate.Value];
            Assert.Contains(actual, possibleValues);
        }
        else
        {
            Assert.Equal(expected, actual);
        }
    }

    [Theory]
    [InlineData(36,31, null)]
    [InlineData(24,23, null)]
    [InlineData(6,7, null)]
    [InlineData(98,97, null)]
    [InlineData(30,29, 31)]
    [InlineData(26,23, 29)]
    [InlineData(14,13, null)]
    [InlineData(15,13, 17)]
    [InlineData(16,17, null)]
    public void FindClosestToTargetBSearchTest( int target, int expected, int? alternate)
    {
        int actual = Node.FindClosestToTargetBSearch(target, Root);
        if (alternate.HasValue)
        {
            int[] possibleValues = [expected, alternate.Value];
            Assert.Contains(actual, possibleValues);
        }
        else
        {
            Assert.Equal(expected, actual);
        }
    }
}
