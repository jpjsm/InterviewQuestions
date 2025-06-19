using System;
using Xunit;
using FindMedianValueOfTwoSortedLists;
using System.Collections.Generic;

namespace UnitTests
{
    public class UnitTestBSearch
    {
        [Fact]
        public void BasicTestInt()
        {
            int[] list = { 0, 2, 4, 6, 8, 10, 12, 14, 16 };
            (int argument, int expected)[] testcases = { (-1, -1), (0, 0), (1,-1), (8, 4), (9, -1), (10, 5), (15, -1), (16, 8), (17, -1) };
            foreach ((int argument, int expected) test in testcases)
            {
                Assert.Equal<int>(test.expected, FindMedianValueOfTwoSortedLists.Utils.BSearch(list, test.argument));
            }
        }

        [Fact]
        public void BasicTestString()
        {
            List<string> list = new List<string>() { "A", "C", "E", "G", "I", "K", "M", "O", "Q" };
            (string argument, int expected)[] testcases = { (" ", -1), ("A", 0), ("B", -1), ("I", 4), ("J", -1), ("K", 5), ("P", -1), ("Q", 8), ("a", -1) };
            foreach ((string argument, int expected) test in testcases)
            {
                Assert.Equal<int>(test.expected, FindMedianValueOfTwoSortedLists.Utils.BSearch(list, test.argument));
            }
        }

        [Fact]
        public void EmptyList()
        {
            double[] list = null;
            Assert.Equal(-1, FindMedianValueOfTwoSortedLists.Utils.BSearch(list, 1.0));

            list = Array.Empty<double>();
            Assert.Equal(-1, FindMedianValueOfTwoSortedLists.Utils.BSearch(list, 1.0));
        }

        [Fact]
        public void SingletonList()
        {
            bool[] list = new bool[1] { true };
            Assert.Equal(0, FindMedianValueOfTwoSortedLists.Utils.BSearch(list, true));

            Assert.Equal(-1, FindMedianValueOfTwoSortedLists.Utils.BSearch(list, false));
        }

        [Fact]
        public void DoubletonList()
        {
            char[] list = new char[2] { 'a', 'c' };
            (char argument, int expected)[] testcases = { (' ', -1), ('a', 0), ('b', -1), ('c', 1), ('~', -1) };
            foreach ((char argument, int expected) test in testcases)
            {
                Assert.Equal<int>(test.expected, FindMedianValueOfTwoSortedLists.Utils.BSearch(list, test.argument));
            }
        }
    }
}

