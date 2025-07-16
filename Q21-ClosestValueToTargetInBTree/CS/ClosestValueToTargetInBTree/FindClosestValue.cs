
namespace FindClosestValue
{
    public class Node
    {
        private int _value;
        private Node? _left = null;
        private Node? _right = null;

        public int Value => _value;
        public Node? Left
        {
            get { return _left; }
            set
            {
                if (Object.ReferenceEquals(this, value)) throw new ArgumentOutOfRangeException("Circular (infinite) reference.");
                _left = value;
            }
        }
        public Node? Right
        {
            get { return _right; }
            set
            {
                if (Object.ReferenceEquals(this, value)) throw new ArgumentOutOfRangeException("Circular (infinite) reference.");
                _right = value;
            }
        }

        public Node(int value)
        {
            _value = value;
        }

        public void Insert(int newValue)
        {
            if (newValue < _value)
            {
                if (_left == null)
                {
                    _left = new Node(newValue);
                }
                else
                {
                    _left.Insert(newValue);
                }
            }
            else
            {
                if (_right == null)
                {
                    _right = new Node(newValue);
                }
                else
                {
                    _right.Insert(newValue);
                }
            }
        }

        public List<int> ListAscending()
        {
            List<int> values = new List<int>();
            if (_left != null) values.AddRange(_left.ListAscending());
            values.Add(_value);
            if (_right != null) values.AddRange(_right.ListAscending());

            return values;
        }

        public static int FindClosestValueIterative(int target, Node? root)
        {
            
            int minDistance = Math.Abs(target - root.Value);
            int closestValue = root.Value;
            Node? current = root;
            int distance;
            while (current != null)
            {
                distance = Math.Abs(target - current.Value);
                if (distance < minDistance)
                {
                    minDistance = distance;
                    closestValue = current.Value;
                }

                if (target == current.Value) return current.Value;

                if (target < current.Value)
                {
                    current = current.Left;
                }
                else
                {
                    current = current.Right;
                }
            }

            return closestValue;
        }

        public static int FindClosestToTargetBSearch(int target, Node root)
        {
            List<int> orderedAscending = root.ListAscending();
            int closest = orderedAscending.BinarySearch(target);
            if (closest >= 0) return target; // positive indexes mean exact matches.

            // The bitwise negation returns the index of the closest larger than target element
            closest = ~closest;
            if (closest == 0) return orderedAscending[0]; // target is smaller than the smallest item in the tree
            if (closest >= orderedAscending.Count) return orderedAscending[orderedAscending.Count - 1];

            int left = orderedAscending[closest - 1];
            int right = orderedAscending[closest];

            int deltaLeft = Math.Abs(target - left);
            int deltaRight = Math.Abs(target - right);
            return deltaLeft < deltaRight ? left : right;
        }

    }

    
}