# [Array Inversion Count](https://app.codility.com/programmers/trainings/4/array_inversion_count/)

> Copyright 2009–2025 by Codility Limited. All Rights Reserved.
Unauthorized copying, publication or disclosure prohibited.

An array A consisting of N integers is given. An inversion is a pair of indexes
(P, Q) such that P < Q and A[Q] < A[P].

Using Java21, write a function:

`class Solution { public int solution(int[] A); }`

that computes the number of inversions in A, or returns −1 if it exceeds
1,000,000,000.

For example, in the following array:

```java
 A[0] = -1
 A[1] = 6
 A[2] = 3
 A[3] = 4
 A[4] = 7
 A[5] = 4
```

there are four inversions:

(1,2)  (1,3)  (1,5)  (4,5)

so the function should return 4.

Write an efficient algorithm for the following assumptions:

- N is an integer within the range [0..100,000]
- Each element of array A is an integer within the range
[−2,147,483,648..2,147,483,647].
