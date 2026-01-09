from typing import Any, List, Optional, Tuple
from math import log2
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


def CountNodes(node: Node) -> int:
    if node == None:
        return 0

    rcount = 0
    if node.Rnode:
        rcount = CountNodes(node.Rnode)

    lcount = 0
    if node.Lnode:
        lcount = CountNodes(node.Lnode)

    return 1 + rcount + lcount


def TreeMaxDepth(node: Node) -> int:
    def _TreeMaxDepth(node: Node, count: int) -> int:
        if node is None:
            return count

        return max(
            _TreeMaxDepth(node.Lnode, count + 1), _TreeMaxDepth(node.Rnode, count + 1)
        )

    if node is None or not isinstance(node, Node):
        raise ValueError("Not a valid Tree")

    return _TreeMaxDepth(node, 0)


def IsTreeBalanced(node: Node) -> bool:
    """Returns True if the tree is height-balanced

    Args:
        node (Node): The tree to evaluate

    Raises:
        ValueError: When argument is None or not of type Node

    Returns:
        bool: True if the tree is height-balanced
    """
    if node is None or not isinstance(node, Node):
        raise ValueError("Node a valid Tree")

    ncount = CountNodes(node)
    maxdepth = TreeMaxDepth(node)
    l2 = int(log2(ncount)) + 1
    return l2 == maxdepth


def is_balanced(root):
    """
    Returns True if the tree is height-balanced.
    """

    def check(node):
        # Returns the height if balanced, or -1 if not balanced
        if node is None:
            return 0

        left_h = check(node.Lnode)
        if left_h == -1:
            return -1  # left subtree not balanced

        right_h = check(node.Rnode)
        if right_h == -1:
            return -1  # right subtree not balanced

        if abs(left_h - right_h) > 1:
            return -1  # current node not balanced

        return max(left_h, right_h) + 1

    return check(root) != -1


if __name__ == "__main__":
    l = [40, 63, 30, 21, 23, 32, 53]
    sorted_l = sorted(l)
    balanced = FromListToBinaryTree(sorted_l)
    parent_child_list = GenerateDagEdges(balanced)

    graph = graphviz.Digraph(format="jpg")

    for p, c in parent_child_list:
        parent = str(p)
        graph.node(parent)
        if c:
            child = str(c)
            graph.node(child)
            graph.edge(parent, child)

    graph.render("Balanced_Binary_Tree", view=False)

    l += [1, 60]
    sorted_l = sorted(l)
    balanced2 = FromListToBinaryTree(sorted_l)
    parent_child_list = GenerateDagEdges(balanced2)

    graph = graphviz.Digraph(format="jpg")

    for p, c in parent_child_list:
        parent = str(p)
        graph.node(parent)
        if c:
            child = str(c)
            graph.node(child)
            graph.edge(parent, child)

    graph.render("Partial_Full_Balanced_Binary_Tree", view=False)

    unbalanced = Node(4)
    n1 = Node(1)
    n2 = Node(2)
    n2.Lnode = n1
    n3 = Node(3)
    n3.Lnode = n2
    unbalanced.Lnode = n3
    n7 = Node(7)
    n6 = Node(6)
    n6.Rnode = n7
    n5 = Node(5)
    n5.Rnode = n6
    unbalanced.Rnode = n5
    parent_child_list = GenerateDagEdges(unbalanced)

    graph = graphviz.Digraph(format="jpg")

    for p, c in parent_child_list:
        parent = str(p)
        graph.node(parent)
        if c:
            child = str(c)
            graph.node(child)
            graph.edge(parent, child)

    graph.render("Un-balanced_Binary_Tree", view=False)

    print("Testing IsBalancedTree")
    balancedtests = [(balanced, True), (balanced2, True), (unbalanced, False)]

    for t, e in balancedtests:
        r = IsTreeBalanced(t)
        if e != r:
            print(f"IsTreeBalanced: Actual value '{r}' different than expected '{e}'")

        r = is_balanced(t)
        if e != r:
            print(f"is_balanced: Actual value '{r}' different than expected '{e}'")

    print("Tests completed")
