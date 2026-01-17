#!/usr/bin/env python3
from __future__ import annotations
from typing import List, Optional


class Node:
    def __init__(self, value):
        self.Value = value

        self.Lnode: Optional[Node] = None
        self.Rnode: Optional[Node] = None

    @staticmethod
    def IsSymmetric(node: Optional[Node]) -> bool:
        def mirror(l: Optional[Node], r: Optional[Node]):
            if l is None and r is None:
                return True
            if l is None or r is None:
                return False

            return (
                l.Value == r.Value
                and mirror(l.Lnode, r.Rnode)
                and mirror(l.Rnode, r.Lnode)
            )

        return mirror(node.Lnode, node.Rnode)

    def IsPalindromicTree(self) -> bool:
        def _IsPalindromic(l):
            half = len(l) >> 1  # fast divide by 2
            for i in range(0, half + 1):
                if l[i] != l[len(l) - 1 - i]:
                    return False
            return True

        def _Split(node: Node) -> List[str]:
            if node is None:
                return []

            if not isinstance(node, Node):
                raise ValueError("'node'argument must be of Node type")

            return _Split(node.Lnode) + [str(node.Value)] + _Split(node.Rnode)

        items = _Split(self)
        return _IsPalindromic(items)


if __name__ == "__main__":
    print("... starting ...")
    l_5 = Node(5)
    l_4 = Node(4)
    l_4.Lnode = Node(1)
    l_4.Rnode = Node(2)

    l_2 = Node(2)
    l_2.Lnode = l_5
    l_2.Rnode = l_4

    r_4 = Node(4)
    r_4.Lnode = Node(2)
    r_4.Rnode = Node(1)

    r_5 = Node(5)

    r_2 = Node(2)
    r_2.Lnode = r_4
    r_2.Rnode = r_5

    root = Node(3)
    root.Lnode = l_2
    root.Rnode = r_2

    print(f"Is root a palindromic tree: {root.IsPalindromicTree()}")
    print(f"Is 'root'a symmetric tree: {Node.IsSymmetric(root)}")
    print("... finished ...")
