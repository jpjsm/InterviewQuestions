using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace UnitCombinationsToTarget
{
    class Program
    {
        static void Main(string[] args)
        {
            UnitCombinations foo;
            foo = new UnitCombinations(5, new uint[] { 1, 2, 3 });
            Console.WriteLine("Possible answers: {0}", foo.Results != null ? foo.Results.Count : 0);

            foo = new UnitCombinations(5, new uint[] { 2, 3 });
            Console.WriteLine("Possible answers: {0}", foo.Results != null ? foo.Results.Count : 0);

            foo = new UnitCombinations(5, new uint[] { 2 });
            Console.WriteLine("Possible answers: {0}", foo.Results != null ? foo.Results.Count : 0);
        }
    }

    public class UnitCombinations
    {
        private class Node
        {
            public uint Value { get; set; }
            public uint Unit { get; set; }
            public Node Parent { get; set; }
            public List<Node> Children { get; set; }

            public Node(uint v, Node p)
            {
                this.Value = v;
                this.Parent = p;
                this.Children = new List<Node>();
            }
        }

        public uint[] Units { get; private set; }
        public uint[] ExcludedUnits { get; private set; }
        public uint Target { get; private set; }
        public List<List<uint>> Results { get; private set; }

        public UnitCombinations(uint target, uint[] units)
        {
            // Validate input
            // target > 0
            // units not null or empty; and, unit values > 0 and values <= target

            this.Target = target;
            this.Units = units.Where(v => v > 0 && v <= target).OrderBy(v => v).ToArray();
            this.ExcludedUnits = units.Except(this.Units).ToArray();
            int unitsLength = this.Units.Length;

            // build reduction map
            Dictionary<uint, uint[]> reductionMap = new Dictionary<uint, uint[]>();
            Queue<uint> localTargets = new Queue<uint>();
            localTargets.Enqueue(this.Target);
            uint currentTarget;
            while (localTargets.Count > 0)
            {
                currentTarget = localTargets.Dequeue();
                if (!reductionMap.ContainsKey(currentTarget))
                {
                    uint[] goals = new uint[unitsLength];
                    for (int i = 0; i < unitsLength; i++)
                    {
                        if (currentTarget > this.Units[i])
                        {
                            goals[i] = currentTarget - this.Units[i];
                            localTargets.Enqueue(goals[i]);
                        }
                    }

                    reductionMap.Add(currentTarget, goals);
                }
            }

            // Seed paths queue with all nodes reachable from Zero
            Node zero = new Node(0, null);
            Queue<Node> paths = new Queue<Node>();
            for (int i = 0; i < unitsLength; i++)
            {
                if (reductionMap.ContainsKey(this.Units[i]))
                {
                    Node newChild = new Node(this.Units[i], zero);
                    newChild.Unit = this.Units[i];
                    zero.Children.Add(newChild);
                    paths.Enqueue(newChild);
                }
            }

            // Traversing reductionMap bottom up
            Node currentNode;
            List<Node> resultNodes = new List<Node>();
            while (paths.Count > 0)
            {
                currentNode = paths.Dequeue();
                if (currentNode.Value == this.Target)
                {
                    resultNodes.Add(currentNode);
                    continue;
                }

                for (int i = 0; i < unitsLength; i++)
                {
                    if (reductionMap.ContainsKey(this.Units[i] + currentNode.Value))
                    {
                        Node newChild = new Node(this.Units[i] + currentNode.Value, currentNode);
                        newChild.Unit = this.Units[i];
                        newChild.Children.Add(newChild);
                        paths.Enqueue(newChild);
                    }
                }
            }

            if(resultNodes.Count > 0)
            {
                this.Results = new List<List<uint>>();
            }

            foreach (var resultNode in resultNodes)
            {
                List<uint> result = new List<uint>();
                currentNode = resultNode;
                do
                {
                    result.Add(currentNode.Unit);
                    currentNode = currentNode.Parent;
                } while (currentNode.Parent != null);

                this.Results.Add(result);
            }

        }
    }
}
