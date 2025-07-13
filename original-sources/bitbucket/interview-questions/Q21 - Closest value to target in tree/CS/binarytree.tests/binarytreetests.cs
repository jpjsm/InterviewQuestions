namespace binarytree.tests;

public class BinaryTreeTests
{
    [Theory]
    [InlineData(new int[] { 8, 5, 12, -1, 7}, 8, 8)]
    [InlineData(new int[] { 8, 5, 12, -1, 7}, -4, -1)]
    [InlineData(new int[] { 8, 5, 12, -1, 7}, 6, 7)]
    public void FindClosestToTargetTest(int[] values, int target, int expected)
    {
        Node btree = new Node(values[0]);
        for (int i = 1; i < values.Length; i++)
        {
            btree.Insert(values[i]);            
        }


        Assert.Equal(expected, btree.FindClosestToTarget(target));
    }
}
