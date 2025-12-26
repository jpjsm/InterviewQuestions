from typing import Any, List, Set, Tuple


def combinations(
    items: List[Any] | Tuple[Any, ...] | Set[Any], length: int
) -> List[List[Any]]:
    if length < 0:
        raise ValueError("Length must be a positive number.")

    if length == 0 or length > len(items):
        return [[]]

    items_l = list(i for i in items)
    if length == len(items):
        return [items_l.copy()]

    # Combinations with first item of the list
    combinations_with_first = [
        [items_l[0]] + reduced_combinations
        for reduced_combinations in combinations(items_l[1:], length - 1)
    ]
    # Combinations without first item of thelist
    combinations_without_first = combinations(items_l[1:], length)

    return combinations_with_first + combinations_without_first


def permutations(
    items: List[Any] | Tuple[Any, ...] | Set[Any],
    length: int,
    repetitions: bool = False,
    used_indices: Set[int] = set(),
) -> List[List[Any]]:
    if length < 0:
        raise ValueError("Length must be a positive number.")

    if (length > len(items)) and not repetitions:
        raise ValueError(
            "Too few items to generate 'length' permutations without repetitions"
        )

    if length == 0:
        return [[]]

    items_l = list(i for i in items)

    results = []
    for i in range(len(items_l)):
        if not repetitions and i in used_indices:
            continue
        new_used: Set[int] = {i} | used_indices
        perms = permutations(items_l, length - 1, repetitions, new_used)
        for perm in perms:
            results.append([items_l[i]] + perm)

    return results


if __name__ == "__main__":
    items = [1, 2, 3, 4, 5]
    combs = combinations(items, 3)
    for comb in sorted(combs):
        print(comb)

    items = [0, 1]
    perms = permutations(items, 4, True)
    for perm in perms:
        print(perm)

    items = ["a", "b", "c", "d"]
    perms = permutations(items, 3)
    for perm in perms:
        print(perm)
