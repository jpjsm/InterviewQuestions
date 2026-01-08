from typing import Any, List, Optional, Tuple


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


def Distance(a, b) -> float:
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(a - b)

    raise ValueError(f"Distance not defined for {type(a)} and {type(b)}")


def ClosestInBTree(node, target, distance):
    def _BTreeClosest(node, target, distance, min_distance, candidate):
        if node is None:
            return candidate

        if node.Value == target:
            return target

        current_distance = distance(target, node.Value)
        if current_distance < min_distance:
            min_distance = current_distance
            candidate = node.Value

        if target > node.Value:
            return _BTreeClosest(node.Rnode, target, distance, min_distance, candidate)

        return _BTreeClosest(node.Lnode, target, distance, min_distance, candidate)

    if node is None or not isinstance(node, Node):
        raise ValueError("node is undefined")

    if target is None:
        raise ValueError("target is undefined")

    if node.Value == target:
        return target

    min_distance = distance(target, node.Value)
    candidate = node.Value
    return _BTreeClosest(node, target, distance, min_distance, candidate)


def ExistsInBTree(node, target) -> bool:
    def _BTreeExisits(node, target) -> bool:
        if node is None:
            return False

        if node.Value == target:
            return True

        if target > node.Value:
            return _BTreeExisits(node.Rnode, target)

        return _BTreeExisits(node.Lnode, target)

    if node is None or not isinstance(node, Node) or target is None:
        return False

    if node.Value == target:
        return True

    return _BTreeExisits(node, target)


def FloorInBTree(node, target):
    def _FloorInBTree(node, target, candidate):
        if node is None:
            return candidate

        if node.Value == target:
            return target

        if candidate is None and node.Value < target:
            candidate = node.Value
        if candidate is not None and node.Value < target and candidate < node.Value:
            candidate = node.Value

        if target > node.Value:
            return _FloorInBTree(node.Rnode, target, candidate)

        return _FloorInBTree(node.Lnode, target, candidate)

    if node is None or not isinstance(node, Node) or target is None:
        raise ValueError("Invalid arguments")

    return _FloorInBTree(node, target, None)


def CeilingInBTree(node, target):
    def _CeilingBTree(node, target, candidate):
        if node is None:
            return candidate

        if target == node.Value:
            return target

        if candidate is None and node.Value > target:
            candidate = node.Value

        if candidate is not None and node.Value > target and node.Value < candidate:
            candidate = node.Value

        if target > node.Value:
            return _CeilingBTree(node.Rnode, target, candidate)

        return _CeilingBTree(node.Lnode, target, candidate)

    if node is None or not isinstance(node, Node) or target is None:
        raise ValueError("Invalid arguments")

    return _CeilingBTree(node, target, None)


if __name__ == "__main__":
    l = [40, 63, 30, 21, 23, 32, 53]
    sorted_l = sorted(l)
    print(sorted_l)
    root = FromListToBinaryTree(sorted_l)

    print("Testing Closest")
    ClosestTests = [
        (53, {53}),
        (1, {21}),
        (64, {63}),
        (36, {32, 40}),
    ]

    for t, e in ClosestTests:
        r = ClosestInBTree(root, t, Distance)
        if r not in e:
            print(f"'{r}' not in expected values {e}")

    print("Testing Exists")
    ExistsTests = [
        (53, True),
        (1, False),
        (64, False),
        (36, False),
        (21, True),
        (63, True),
        (23, True),
    ]

    for t, e in ExistsTests:
        r = ExistsInBTree(root, t)
        if r != e:
            print(f"'{r}' not in equal expected  {e}")

    print("Testing Floor")
    FloorTests = [
        (53, 53),
        (1, None),
        (64, 63),
        (31, 30),
        (22, 21),
        (41, 40),
        (55, 53),
        (25, 23),
    ]

    for t, e in FloorTests:
        r = FloorInBTree(root, t)
        if r != e:
            print(f"Floor of '{t}': '{r}', should be {e}")

    print("Testing Ceiling")
    CeilingTests = [
        (64, None),
        (1, 21),
        (55, 63),
        (45, 53),
        (38, 40),
        (22, 23),
        (29, 30),
        (31, 32),
    ]

    for t, e in CeilingTests:
        r = CeilingInBTree(root, t)
        if r != e:
            print(f"Ceiling of '{t}': '{r}', should be {e}")

    print("Testing complete")
