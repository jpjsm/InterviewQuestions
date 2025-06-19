#!/usr/bin/env python3

def SumSubArrays(A,m):
    """
    Sums all possible subarrays of size m in A.

    param: A, the array to sum over
    param: m, the size of the subarrays

    return: an array with the results

    Example:
        A = [1, 4, 9, 16, 25]
        m = 3

        r = [
            14,  # [1,4,9]
            29,  # [4,9,16]
            50,  # [9,16,25]
        ]
    """
    r = [sum(A[0:m])]
    for i in range(1, len(A) - m +1):
        r.append(r[i-1] + A[m+i-1] - A[i-1])

    return r

if (__name__ == "__main__"):
    print("... starting ...")
    A = [1, 4, 9, 16, 25]
    m = 3
    print(SumSubArrays(A,m))
