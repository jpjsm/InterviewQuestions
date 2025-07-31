namespace jpjsm.GetSmallestKItemsFromList;

public static class ListUtils
{
    public static Point[] GetSmallestKItemsFromList(IList<Point> points, int K)
    {
        SortedHeap.SortedHeap<double, Point> heap = new SortedHeap.SortedHeap<double, Point>(K);
        for (int i = 0; i < K && i < points.Count; i++)
        {
            heap.Insert(points[i].DistanceToOrigin(), points[i]);
        }

        if (points.Count <= K) return heap.Values;

        double currentMax = heap.PeekMaxKey();
        for (int i = K; i < points.Count; i++)
        {
            double d = points[i].DistanceToOrigin();
            if (currentMax > d)
            {
                heap.PopMax();
                heap.Insert(d, points[i]);
                currentMax = heap.PeekMaxKey();
            }
        }
        
        return heap.Values;
    }
}
