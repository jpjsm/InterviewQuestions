namespace MergeOverlappingIntervals
{
    public class Program
    {
        public static List<(int startTime, int endTime)> MergeOverlappingIntervals(List<(int startTime, int endTime)> intervals)
        {

            if (intervals == null || intervals.Count == 0)
            {
                return [];
            }

            List<(int startTime, int endTime)> mergedIntervals = new List<(int startTime, int endTime)>();

            // sort intervals
            intervals.Sort();

            // set current interval to first interval
            int currentStart = intervals[0].startTime;
            int currentEnd = intervals[0].endTime;

            for (int i = 1; i < intervals.Count; i++)
            {
                if (intervals[i].startTime > currentEnd) // we can close current interval, save it, and start a new current
                {
                    mergedIntervals.Add((currentStart, currentEnd));
                    currentStart = intervals[i].startTime;
                    currentEnd = intervals[i].endTime;
                    continue;
                }

                if (currentEnd < intervals[i].endTime)
                {
                    currentEnd = intervals[i].endTime;
                }
            }

            mergedIntervals.Add((currentStart, currentEnd));


            return mergedIntervals;
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Begin Merge Overlapping Intervals");
            List<(List<(int startTime, int endTime)> testCase, List<(int startTime, int endTime)> expected)> testCases = new List<(List<(int startTime, int endTime)> testCase, List<(int startTime, int endTime)> expected)>()
            {
                (new List<(int startTime, int endTime)>(){(3,6),(4,8),(9,12)}, new List<(int startTime, int endTime)>(){(3,8),(9, 12)}),
                (new List<(int startTime, int endTime)>(){(3,9),(4,8),(9,12)}, new List<(int startTime, int endTime)>(){(3,12)}),
                (new List<(int startTime, int endTime)>(){(3,6),(4,8),(9,12), (5, 21)}, new List<(int startTime, int endTime)>(){(3,21)}),
            };

            foreach (var (testCase, expected) in testCases)
            {
                string testCaseStr = string.Join(',', testCase.Select(i => $"({i.startTime},{i.endTime})"));

                var actual = MergeOverlappingIntervals(testCase);
                string actualStr = string.Join(',', actual.Select(i => $"({i.startTime},{i.endTime})"));
                string expectedStr = string.Join(',', expected.Select(i => $"({i.startTime},{i.endTime})"));
                if (string.Compare(expectedStr, actualStr) != 0)
                {
                    ConsoleColor currentForeground = Console.ForegroundColor;
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine($"ERROR: {testCaseStr} does not produce {expectedStr} != {actualStr}");
                    Console.ForegroundColor = currentForeground;
                }
                else
                {
                    Console.WriteLine($"OK: {testCaseStr} --> {expectedStr}");

                }
            }


            Console.WriteLine("Completed Merge Overlapping Intervals");
        }
    }
}