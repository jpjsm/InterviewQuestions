# Binary Tree Searches

From a binary tree, find the element in the tree that's closest to a target,
the floor element, the ceiling element.

For example, given the following tree:

![Binary Tree of Integers](<./Binary%20Tree.jpg>)

In `FindClosest(t)`:

| target | answer |
| :---: | :---: |
| 53 | 53 |
| 1 | 21 |
| 64 | 63 |
| 36 | 32 or 40 |

In `FindFloor(t)`:

| target | answer |
| :---: | :---: |
| 53 | 53 |
| 1 | null |
| 64 | 63 |
| 36 | 32 |

In `FindCeiling(t)`:

| target | answer |
| :---: | :---: |
| 53 | 53 |
| 1 | 21 |
| 64 | null |
| 36 | 40 |
