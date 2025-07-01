namespace binarytree;

public class Node
{
    private int value;
    private Node? left = null;
    private Node? right = null;

    public Node(int newvalue)
    {
        value = newvalue;
    }

    public void Insert(int newvalue)
    {
        if (newvalue < value)
        {
            if (left == null)
            {
                left = new Node(newvalue);
            }
            else
            {
                left.Insert(newvalue);
            }
        }
        else
        {
            if (right == null)
            {
                right = new Node(newvalue);
            }
            else
            {
                right.Insert(newvalue);
            }
        }
    }

    public List<int> ListAscending()
    {
        List<int> values = new List<int>();
        if (left != null) values.AddRange(left.ListAscending());
        values.Add(value);
        if (right != null) values.AddRange(right.ListAscending());

        return values;
    }

    public int FindClosestToTarget(int target)
    {
        List<int> orderedvalues = this.ListAscending();
        int closest = orderedvalues.BinarySearch(target);
        if (closest >= 0) return target; // positive indexes mean exact matches.
        
        // The bitwise negation returns the index of the closest larger than target element
        closest = ~closest;
        if (closest == 0) return orderedvalues[0]; // target is smaller than the smallest item in the tree
        if (closest >= orderedvalues.Count) return orderedvalues[orderedvalues.Count - 1];

        int left = orderedvalues[closest - 1];
        int right = orderedvalues[closest];

        int deltaleft = Math.Abs(target - left);
        int deltaright = Math.Abs(target - right);
        return deltaleft < deltaright ? left : right;
    }

}
