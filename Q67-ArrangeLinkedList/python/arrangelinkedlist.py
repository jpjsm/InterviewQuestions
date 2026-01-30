from __future__ import annotations
from random import randint
from typing import Any, List, Optional


class Link:
    def __init__(self, value: Any):
        self.Value: Any = value
        self.Next: Optional[Link] = None

    def __str__(self) -> str:
        items = []
        current = self
        while current:
            items.append(str(current.Value))
            current = current.Next

        return f"[{', '.join(items)}]"


def list2links(l: List[Any]) -> Optional[Link]:
    if l is None:
        return None

    if not isinstance(l, (list, tuple)):
        return Link(l)

    if not l:
        return None

    head = Link(l[0])
    current = head
    for i in range(1, len(l)):
        current.Next = Link(l[i])
        current = current.Next
    return head


def ArrangeLinkedList(node: Link, X: Any) -> Optional[Link]:
    def InsertNext(at: Link, next: Link) -> Link:
        # Make 'next' point to what 'at' is pointing to
        next.Next = at.Next
        # Make 'at' point to 'next'
        at.Next = next
        return next

    def PopNext(at: Link) -> Optional[Link]:
        if at.Next is None:
            return None

        old = at.Next

        if old.Next:
            at.Next = old.Next
        else:
            # 'at' is now the end of the list
            at.Next = None

        old.Next = None
        return old

    if node is None or not isinstance(node, Link):
        raise ValueError("'node' not a linked list")

    if node.Next is None:
        return node  # Nothing to arrange

    # Run the list until find First node equal or greater than X
    # - Set last lesser

    # Run the list until the end
    # - Everytime a node is less than X
    #   - Remove node from list
    #   - insert node between last lesser and first equal or greater X
    #   - set last lesser to inserted

    # Caveats !!
    # What to do if 'node.Value' is equal or greater X?
    # Let's have a head of list node pointing to node
    # and make last_lesser point to head

    head: Link = Link(None)
    head.Next = node
    last_lesser = head
    current = node

    # Searching for first equal or greater X
    if node.Value < X:
        while current.Next and current.Next.Value < X:
            current = current.Next

        last_lesser = current

    # Searching for values less or equal X
    # when found move after last_lesser and update last_lesser

    while current and current.Next:
        while current.Next and current.Next.Value >= X:
            current = current.Next

        while current.Next and current.Next.Value < X:
            next_last_lesser = PopNext(current)
            if next_last_lesser:
                last_lesser = InsertNext(last_lesser, next_last_lesser)

    return node if node == head.Next else head.Next


if __name__ == "__main__":
    tests = [
        (([3], 5), [3]),
        (([7], 5), [7]),
        (([1, 2, 3, 4], 5), [1, 2, 3, 4]),
        (([4, 3, 2, 1, 5], 5), [4, 3, 2, 1, 5]),
        (([5, 4], 5), [4, 5]),
        (([9, 8, 7, 6, 5], 5), [9, 8, 7, 6, 5]),
        (([9, 8, 7, 6, 5, 4, 3, 2, 1], 5), [4, 3, 2, 1, 9, 8, 7, 6, 5]),
        (
            ([1, 4, 6, 6, 1, 7, 5, 7, 2, 2, 8, 9, 8, 9, 2, 8], 5),
            [1, 4, 1, 2, 2, 2, 6, 6, 7, 5, 7, 8, 9, 8, 9, 8],
        ),
        (([1, 2, 9, 8, 8, 7, 7, 7, 2], 5), [1, 2, 2, 9, 8, 8, 7, 7, 7]),
        (
            ([5, 6, 5, 5, 1, 2, 6, 8, 6, 2, 6, 6, 5, 4, 2, 8], 5),
            [1, 2, 2, 4, 2, 5, 6, 5, 5, 6, 8, 6, 6, 6, 5, 8],
        ),
        (
            ([6, 1, 2, 8, 2, 4, 8, 7, 9, 4, 2, 5, 6, 7, 7], 5),
            [1, 2, 2, 4, 4, 2, 6, 8, 8, 7, 9, 5, 6, 7, 7],
        ),
        (
            ([1, 8, 6, 8, 2, 1, 1, 7, 4, 2, 9, 5, 8, 8], 5),
            [1, 2, 1, 1, 4, 2, 8, 6, 8, 7, 9, 5, 8, 8],
        ),
    ]

    for (l, X), e in tests:
        nodes = list2links(l)
        r = ArrangeLinkedList(nodes, X)
        if str(r) != str(e):
            print(f"❌\t{r} -> {e}")

    print("Finished Tests")
