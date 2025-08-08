# Sum all node values, in a BST, that are within range

Given a BST, get the sum of all node values that are within range,
both ond of the range included.

Sum(Node node, int min, max)

Example:


Assume the following BST is given with the name of `tree`

```txt
        6
        / \
       4   12
      / \ 
     3   5
    /
   2
```
The evaluation of `Sum(node, 2, 5) ==> 14`