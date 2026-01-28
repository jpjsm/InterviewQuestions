"""Return the k-th row in a Pascal's Triangle

# Analysis

## Alternative A
----------------
The triangle can be built iteratively until the k-th row is generated
The triangle can be initialized with the first three rows
  [
      [1],
     [1, 1],
    [1, 2, 1]
  ]

Next row items can be defined as:
next_row[0] = 1
next_row[i] = prev_row[i-1] + prev_row[i] ; for 0 < i < row_number
next_row.append(1)

## Alternative B
----------------
Also, each row in the triangle correspond to the binomial coeficients of the
power of the row... this could be an easier way to get those numbers, if we
only need the k-th row.

The row values are given by (n k) = n! / (k! * (n-k)!)
"""

import math
from typing import List


def PascalTriangleRow1(k: int) -> List[int]:
    if not isinstance(k, int) or k < 0:
        raise ValueError("Invalid argument 'k', it must be a positive integer or zero.")
    row = []
    for i in range(k):
        row.append(math.comb(k, i))

    row.append(1)
    return row


def PascalTriangleRow2(k: int) -> List[int]:
    rows: List[List[int]] = [[1], [1, 1], [1, 2, 1]]
    while k >= len(rows):
        # Add next row
        lastrow = len(rows) - 1
        nextrow = [1]
        for i in range(1, len(rows)):
            nextrow.append(rows[lastrow][i - 1] + rows[lastrow][i])
        nextrow.append(1)
        rows.append(nextrow)

    return rows[k]


if __name__ == "__main__":
    tests = [
        (0, [1]),
        (1, [1, 1]),
        (2, [1, 2, 1]),
        (3, [1, 3, 3, 1]),
        (6, [1, 6, 15, 20, 15, 6, 1]),
        (7, [1, 7, 21, 35, 35, 21, 7, 1]),
        (
            20,
            [
                1,
                20,
                190,
                1140,
                4845,
                15504,
                38760,
                77520,
                125970,
                167960,
                184756,
                167960,
                125970,
                77520,
                38760,
                15504,
                4845,
                1140,
                190,
                20,
                1,
            ],
        ),
    ]

    for testfunction in [PascalTriangleRow1, PascalTriangleRow2]:
        for k, e in tests:
            r = testfunction(k)
            if r != e:
                print(
                    f"[ERROR {testfunction.__name__}] result row {r} != {e} expected."
                )
            # else:
            #     print(f"[{testfunction.__name__}] k: {k} -> {r} ✅")

        print(f"[{testfunction.__name__}] Tests Completed !! ✅✅")
