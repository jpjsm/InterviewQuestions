using jpjsm.GetSmallestKItemsFromList;

namespace jpjsm.EvaluateGetSmallestKItemsFromList
{
    public class EvaluateGetSmallestKItemsFromList
    {
        private static readonly Random rnd = new Random();
        private static (double distance, Point point)[] points = new (double distance, Point point)[MAXARRAYSIZE];
        private static (double distance, Point point)[] pointsAscending = new (double distance, Point point)[MAXARRAYSIZE];
        public const int MAXARRAYSIZE = 16_000_000;

        static void Main(string[] args)
        {
            Console.WriteLine("********************************************************************************************************");
            Console.WriteLine($"********************************** {DateTime.Now.ToString("o")} **********************************");

            string resultspath = $"results_{DateTime.Now.ToString("yyyyMMdd_HHmmssfffffzz")}.csv";
            using (StreamWriter writer = File.AppendText(resultspath))
            {
                writer.WriteLine($"testId,method,arraySize,subsetSize,repetitionId,beginTestTicks,endTestTicks,elapsedTicks,elapsedMilliseconds");
            }

            int testRuns = 20;
            int arraySize = MAXARRAYSIZE;
            List<int> sizes = new List<int>();
            while (arraySize >= 10_000)
            {
                sizes.Add(arraySize);
                arraySize >>= 1;
            }
            int[] N = sizes.ToArray();
            int[] K = [11, 19, 41, 79, 157, 307, 619];
            int repetitions = 20;

            int maxPointCount = N.Max();
            (long beginTestTicks, long endTestTicks) timer;
            //(string method, int arraySize, int subsetSize, int repetition, long beginTestTicks, long endTestTicks, long elapsedTicks)
            for (int t = 0; t < testRuns; t++)
            {
                GenerateRandomPoints(points, int.MinValue, int.MaxValue, int.MinValue, int.MaxValue);

                foreach (int n in N)
                {
                    foreach (int k in K)
                    {
                        for (int i = 0; i < repetitions; i++)
                        {
                            timer = FindKSmallestPointsSorting(points, n, k);

                            using (StreamWriter writer = File.AppendText(resultspath))
                            {
                                TimeSpan elapsed = new TimeSpan(timer.endTestTicks - timer.beginTestTicks);
                                writer.WriteLine($"{t},sorting,{n},{k},{i + 1},{timer.beginTestTicks},{timer.endTestTicks},{timer.endTestTicks - timer.beginTestTicks},{elapsed.TotalMilliseconds}");
                                Console.WriteLine($"{t},sorting,{n},{k},{i + 1},{timer.beginTestTicks},{timer.endTestTicks},{timer.endTestTicks - timer.beginTestTicks},{elapsed.TotalMilliseconds}");
                            }

                            timer = FindKSmallestPointsHeapSorting(points, n, k);

                            using (StreamWriter writer = File.AppendText(resultspath))
                            {
                                TimeSpan elapsed = new TimeSpan(timer.endTestTicks - timer.beginTestTicks);
                                writer.WriteLine($"{t},heap,{n},{k},{i + 1},{timer.beginTestTicks},{timer.endTestTicks},{timer.endTestTicks - timer.beginTestTicks},{elapsed.TotalMilliseconds}");
                                Console.WriteLine($"{t},heap,{n},{k},{i + 1},{timer.beginTestTicks},{timer.endTestTicks},{timer.endTestTicks - timer.beginTestTicks},{elapsed.TotalMilliseconds}");
                            }
                        }
                    }
                }
            }

            Console.WriteLine($"********************************** {DateTime.Now.ToString("o")} **********************************");
            Console.WriteLine("********************************************************************************************************");
        }

        public static (long startTick, long endTick) FindKSmallestPointsSorting((double distance, Point point)[] points, int count, int k)
        {
            Array.Copy(points, pointsAscending, count);
            long startTick = DateTime.Now.Ticks;
            Array.Sort(pointsAscending,0,count, Comparer<(double distance, Point point)>.Create((a, b) => a.distance.CompareTo(b.distance)));
            (double distance, Point point)[] kSmallestPoints = pointsAscending.Take(k).ToArray();
            long endTick = DateTime.Now.Ticks;

            // forcing the compiler to generate kSmallestPoints
            using (StreamWriter writer = StreamWriter.Null)
            {
                writer.WriteLine(string.Join(",", kSmallestPoints.Select(p => p.point.ToString())));
            }
            return (startTick, endTick);
        }

        public static (long startTick, long endTick) FindKSmallestPointsHeapSorting((double distance, Point point)[] points, int count, int k)
        {
            Point[] values = points.Take(count).Select(p => p.point).ToArray();

            long startTick = DateTime.Now.Ticks;
            Point[] kSmallestPoints = ListUtils.GetSmallestKItemsFromList(values, k);
            long endTick = DateTime.Now.Ticks;

            // forcing the compiler to generate kSmallestPoints
            using (StreamWriter writer = StreamWriter.Null)
            {
                writer.WriteLine(string.Join(",", kSmallestPoints.Select(p => p.ToString())));
            }
            return (startTick, endTick);
        }
        public static void GenerateRandomPoints((double distance, Point point)[] data, int lowestX, int maxX, int lowestY, int maxY)
        {
            int length = data.Length;

            for (int i = 0; i < length; i++)
            {
                Point point = new Point(rnd.Next(lowestX, maxX), rnd.Next(lowestY, maxY));
                data[i] = (point.DistanceToOrigin(), point);
            }
        }
    }

}

