using System.Transactions;

namespace GetNthToLastFromLinkedList
{
    public class Link
    {
        private char _value;
        private Link? _next = null;

        public Link? Next
        {
            get { return _next; }
            set
            {
                if (value == null || value is Link)
                {
                    _next = value;
                }
                else
                {
                    throw new ArgumentException($"{nameof(value)}  must be of type Link.");
                }
            }
        }

        public char Value => _value;

        public Link(char value)
        {
            _value = value;
        }
    }
    public class LinkedList
    {
        private Link? _head = null;

        public Link? Head => _head;

        public LinkedList()
        {

        }

        public void Insert(char value)
        {
            Link link = new Link(value);

            if (_head != null)
            {
                link.Next = _head;
            }

            _head = link;
        }

        public IEnumerable<char> Scan()
        {
            Link? current = _head;

            while (current != null)
            {
                yield return current.Value;
                current = current.Next;
            }
        }

        public void RemoveDuplicates()
        {
            if (_head == null) return;

            HashSet<char> uniqueValues = new HashSet<char>();
            uniqueValues.Add(_head.Value);
            Link? previous = _head;
            Link? current = previous.Next;
            while (current != null)
            {
                if (!uniqueValues.Contains(current.Value))
                {
                    uniqueValues.Add(current.Value);
                    previous.Next = current;
                    previous = current;
                }
                else
                {
                    current = current.Next;
                }

            }

            previous.Next = null;
        }

        public char NthToLast(int n)
        {
            // if list empty or length < n throw exception
            if (_head == null) throw new Exception("Empty list.");
            int i = 0;
            Link? runner = _head;
            Link? current = runner;
            while (runner != null && i < n)
            {
                runner = runner.Next;
                i++;
            }

            if (i < n) throw new Exception($"List is shorter than 'n': {i} < {n}.");

            while (runner.Next != null)
            {
                runner = runner.Next;
                current = current.Next; 
            }
            
            return current.Value;
        }
    }
}

