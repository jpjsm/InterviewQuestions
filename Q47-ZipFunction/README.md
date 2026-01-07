# Zip function

Given a linked-list of linked-lists of object, transpose the objects
into a linked list of linked lists up to the first list that run out of
items.

The argument to the function should remain unchanged after the function returns.

For example, given the following list of lists:

```txt
↓
1 → 2 → 3 → 4
↓
A → B → C
↓
a → b → c → d
_
```

Return:

```txt
↓
1 → A → a
↓
2 → B → b
↓
3 → C → c
_
```
