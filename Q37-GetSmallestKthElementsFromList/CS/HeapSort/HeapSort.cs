namespace jpjsm.SortedHeap;

public class SortedHeap<K, T> where K : struct, IComparable
{
    private (K key, T data)[] heap;
    private int count = 0;

    public int Count => count;

    public bool Empty => count == 0;

    public int MaxCapacity => heap.Length;

    public T[] Values => heap.Take(count).Select(kv => kv.data).ToArray();

    public SortedHeap(int size)
    {
        ArgumentOutOfRangeException.ThrowIfLessThanOrEqual(size, 0, nameof(size));
        heap = new (K, T)[size];
    }

    public bool Insert(K key, T data)
    {
        if (count >= MaxCapacity) return false;
        heap[count++] = (key, data);
        FixUp(count-1);
        return true;
    }

    public (K, T) PopMax()
    {
        if (Empty) throw new ApplicationException("Cannot remove MAX from empty list.");
        Swap(0, count - 1);
        FixDown(count - 2);
        (K key, T data) = heap[count-1];
        count--;
        return (key, data);
    }

    public K PeekMaxKey()
    {
        return heap[0].key;
    }

    public T PeekMaxKeyData()
    {
        return heap[0].data;
    }

    private void Swap(int i, int j)
    {
        if (i == j) return;
        (heap[i], heap[j]) = (heap[j], heap[i]);
    }

    private void FixDown(int N)
    {
        int k = 0;
        while ((k << 1) < N)
        {
            int j = k == 0? 1: k << 1; // fastest multiply by 2
            if (j < N && heap[j].key.CompareTo(heap[j + 1].key) < 0)
                j++;

            if (!(heap[k].key.CompareTo(heap[j].key) < 0))
                break;

            Swap(k, j);
            k = j;
        }
    }

    private void FixUp(int l)
    {
        while (l > 0 && heap[l / 2].key.CompareTo(heap[l].key) < 0)
        {
            Swap(l / 2, l);
            l >>= 1; // fastest division by 2
        }
    }
}
