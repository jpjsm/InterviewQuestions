from __future__ import annotations
from typing import Any, List


class Node:
    def __init__(self, value):
        self.Value = value
        self.Lnode: Node = None
        self.Rnode: Node = None


def preordertraversal(node: Node) -> List[Any]:
    if node is None:
        return []

    return [node.Value] + preordertraversal(node.Lnode) + preordertraversal(node.Rnode)


def preordertraversalprint(node: Node):
    if node is None:
        return

    print(node.Value)
    preordertraversalprint(node.Lnode)
    preordertraversalprint(node.Rnode)


if __name__ == "__main__":
    n002 = Node(2)
    n003 = Node(3)
    n005 = Node(5)
    n005.Lnode = n002
    n005.Rnode = n003

    n007 = Node(7)
    n013 = Node(13)
    n017 = Node(17)
    n017.Lnode = n007
    n017.Rnode = n013

    n011 = Node(11)
    n011.Lnode = n005
    n011.Rnode = n017

    print(preordertraversal(n011))

    preordertraversalprint(n011)
