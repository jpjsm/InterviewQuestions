# Tree Preorder Traversal

Informally, a preorder traversaql involves "walking"around the binary-tree in a
counterclock-wise manner; starting at the root, sticking closely to the
edges, and printing out the nodes as you encounter them.

Write a function that returns a list of all nodes in a binary-tree in preorder
traversal.

Given the following tree:

```txt
                                     59
                                   /    \
                 /                                \
          23                                             101
        /    \                                         /     \
    /            \                                 /             \
   11             37                              79             113
  /  \           /  \                            /  \           /   \
 5    17        29   47                         67   89       107    131
/ \  /  \      /  \  /  \                      /  \ /  \      /  \   /  \
2  3 7  13    19  31 41 53                    61 71 73 83    97 103 109 127
```

The answer should be:

```txt
[59, 23, 11, 5, 2, 3, 17, 7, 13, 37, 29, 19, 31, 47, 41, 53, 101, 79, 67, 61,
71, 89, 73, 83, 113, 107, 97, 103, 131, 109, 127]
```
