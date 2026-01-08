from typing import Any, List, Optional, Tuple

import graphviz


class Node:
    def __init__(self, value):
        self.Value = value
        self.Lnode = None
        self.Rnode = None


def FromListToBinaryTree(l) -> Node | None:
    """Converts a "sorted" list into a balanced binary tree.

    Args:
        l (Any type): a "sorted" list

    Returns:
        Node | None: A balanced binary tree
    """
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
    """Generates a list of tuples: (Parent_value, Child_value); each tuple
    representes an edge in the tree.

    Args:
        node (Node): The parent node to generate the edge tuples, if left or
        right nodes exist.

    Returns:
        list: The list of (Parent_value, Child_value) tuples
    """
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
