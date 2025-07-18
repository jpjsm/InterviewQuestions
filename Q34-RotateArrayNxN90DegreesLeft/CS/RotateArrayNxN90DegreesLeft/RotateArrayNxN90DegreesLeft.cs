namespace RotateArrayNxN90DegreesLeft;

public static class RotateArray
{
    public static int[,] RotateArrayNxN90DegreesLeft(int[,] A)
    {
        ArgumentNullException.ThrowIfNull(A);
        if (A.Rank != 2) throw new ArgumentOutOfRangeException($"'{nameof(A)}' must be a 2 dimensions array.");
        if (A.GetLength(0) != A.GetLength(1)) throw new ArgumentOutOfRangeException($"'{nameof(A)}' must be a square array..");


        int N = A.GetLength(0);
        int ci = 0; // ci --> Corner Index

        while (N > 1)
        {
            int n = N - 1;
            for (int i = 0; i < n; i++)
            {
                int tmp = A[ci, ci + i];
                A[ci, ci + i] = A[ci + i, ci + n];
                A[ci + i, ci + n] = A[ci + n, ci + n - i];
                A[ci + n, ci + n - i] = A[ci + n - i, ci];
                A[ci + n - i, ci] = tmp;
            }

            N -= 2;
            ci++;
        }

        return A;
    }
}
