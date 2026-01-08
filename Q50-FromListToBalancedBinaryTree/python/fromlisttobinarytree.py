from typing import Any, List, Optional, Tuple

import graphviz


class Node:
    def __init__(self, value):
        self.Value = value
        self.Lnode = None
        self.Rnode = None


def FromListToBinaryTree(l) -> Node | None:
    if l is None or not isinstance(l, (list, tuple)):
        return None

    if len(l) == 1:
        return Node(l[0])

    mid = len(l) >> 1  ## Fast div by 2
    node = Node(l[mid])
    node.Lnode = FromListToBinaryTree(l[:mid])
    node.Rnode = FromListToBinaryTree(l[mid + 1 :]) if mid + 1 < len(l) else None
    return node


def GenerateDagEdges(node: Node) -> list:
    if node is None:
        return []

    results = []
    if node.Lnode:
        results += [(node.Value, node.Lnode.Value)] + GenerateDagEdges(node.Lnode)

    if node.Rnode:
        results += [(node.Value, node.Rnode.Value)] + GenerateDagEdges(node.Rnode)

    if node.Lnode is None and node.Rnode is None:
        results = [(node.Value, None)]
    return results


if __name__ == "__main__":
    l = [40, 63, 30, 21, 23, 32, 53]
    sorted_l = sorted(l)
    print(sorted_l)
    root = FromListToBinaryTree(sorted_l)
    parent_child_list = GenerateDagEdges(root)

    print(parent_child_list)

    graph = graphviz.Digraph(format="jpg")

    for p, c in parent_child_list:
        parent = str(p)
        graph.node(parent)
        if c:
            child = str(c)
            graph.node(child)
            graph.edge(parent, child)

    graph.render("Binary Tree", view=True)
