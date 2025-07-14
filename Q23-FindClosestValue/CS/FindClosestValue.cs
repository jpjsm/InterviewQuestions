
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
    }

    class Program
    {
        static void Main(string[] args)
        {
            Node node_13 = new Node(13);
            Node node_23 = new Node(23);
            Node node_47 = new Node(47);
            Node node_71 = new Node(71);
            Node node_97 = new Node(97);

            Node node_89 = new Node(89);
            node_89.Right = node_97;
            node_89.Left = node_71;

            Node node_61 = new Node(61);
            node_61.Left = node_47;
            node_61.Right = node_89;

            Node node_7 = new Node(7);
            node_7.Right = node_13;

            Node node_29 = new Node(29);
            node_29.Left = node_23;

            Node node_17 = new Node(17);
            node_17.Left = node_7;
            node_17.Right = node_29;


            Node root = new Node(31);
            root.Left = node_17;
            root.Right = node_61;

            (int target, int expected)[] testCases = new (int target, int expected)[]
            {
                new(36,31),
                new(24,23),
                new (6,7),
                new (98,97),
                new (30,31),
                new (26,29),
                new (14,13),
                new (15,17),
                new (16,17),
            };

            Console.WriteLine("Begin Task");
            Console.WriteLine(new string('*',120));
            foreach ((int target, int expected) testCase in testCases)
            {
                int actual = FindClosestValue(testCase.target, root);
                if (actual != testCase.expected)
                {
                    Console.WriteLine($"failed test case for target '{testCase.target}': actual -> {actual} vs {testCase.expected} <- expected");
                }
                else
                {
                    Console.WriteLine($"good job! target '{testCase.target}': closest -> {actual}");
                }
            }


            Console.WriteLine(new string('=',120));
            Console.WriteLine("Task Completed");
        }

        public static int FindClosestValue(int target, Node root)
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
    }
}