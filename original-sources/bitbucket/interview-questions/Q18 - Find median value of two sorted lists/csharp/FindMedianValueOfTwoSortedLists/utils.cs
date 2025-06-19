using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FindMedianValueOfTwoSortedLists
{
    public static class Utils
    {
        public static int BSearch<T>(this IList<T> list, T value)
            where T: System.IComparable<T>
        {
            int i = -1;

            if (list == null || list.Count == 0)
            {
                return i;
            }

            if (list.Count == 1)
            {
                if (list[0].CompareTo(value) == 0)
                {
                    i = 0;
                }

                return i;
            }

            int upper = list.Count - 1;
            int lower = 0;
            int compvalue, delta;

            while (upper > lower)
            {
                delta = (upper - lower) / 2;
                i = lower + delta;

                compvalue = list[i].CompareTo(value);
                switch (compvalue)
                {
                    case 0: // list[i] == value
                        return i;

                    case 1:
                        // list[i] > value, aka 'value' is to the left of 'list[i]'
                        // then move upper to i
                        upper = i;
                        break;

                    default:
                        lower = lower != i ? i:i+1;
                        break;
                }
            }


            return list[lower].CompareTo(value) == 0 ? lower : -1;
        }
    }
}
