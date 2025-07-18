namespace RotateArrayNxN90DegreesLeft;

public static class RotateArray
{
    /// <summary>
    /// Rotate square array 90° left.
    /// </summary>
    /// <remarks>
    /// - This method rotates the array in place.
    /// - This method takes O(n) time to execute; where n is the total number of cells in the array.
    /// - This method takes O(1) space to execute; the extra space used is one integer (tmp).
    /// </remarks>
    /// <remarks>
    /// Algorithm:
    /// Imagine the squared array as a collection of concentric rings.
    /// Rotate each ring 90° left.
    /// At each ring, cells are paired in groups of 4 cells.
    /// move the first cell of four to 'tmp'
    /// move the 2nd to 1st, 3rd to 2nd, 4th to 3rd
    /// move 'tmp' to 4th
    /// </remarks>
    /// <param name="A">The square array to rotate.</param>
    /// <returns>The rotated array.</returns>
    /// <exception cref="ArgumentNullException"></exception>
    /// <exception cref="ArgumentOutOfRangeException"></exception>
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
