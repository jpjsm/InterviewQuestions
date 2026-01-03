from typing import Dict, List, Set
from numbers_list import NUMBERS


def GetIndicesOfTripletsWithSumZero(numbers: List[int]) -> List[List[int]]:
    """Find all combinations of three elements in 'numbers' that add to zero,
       and return the indices of those numbers in list (in ascending order).

    Args:
        numbers (List[int]): The numbers list.

    Returns:
        List[List[int]]: The list of triplets that sum zero.

    Strategy:

    Brut-Force:
    ----------
    Run 3 for loops (inside each other) and test all sums. Report successes.

    Big O: n^3
    ************************************************************************
    Minimize runs:
    -------------
    Let's assume that a = numbers[i], b = numbers[j], and c = numbers[k],
    where none of i, j, k are equal to each other.

    The problem: a + b + c = 0
    Could be re-written as: a + b = -c

    We could generate a map of targets (aka -c) pointing to the position on
    the numbers list; each member of the list is a potential target.
    So we create targets as the negative value of the item in the list, and
    associate the position of the item in the list.

    Now we need to find a pair of numbers that when added give a target; to do
    this we take the first target (in targets) as our target T:

    Now we have the new problem: a + b = T  =>  b = T - a

    To solve, we generate a map to find b's: b -> position of a, for all items
    in list except for the position of T.

    Lastly we go over the numbers list to see which items are the the b's map.
    if the item is in the map, we have a pair that makes T, with the index of T
    we have our triplet. Add the triplet to the results.

    We do this for all T and we have all our solution triplets.

    Big O: n^2 + n -> n^2
    """
    triplets: List[List[int]] = []
    used_indices: Set[int] = set()
    targets: Dict[int, Set[int]] = {}
    for index, number in enumerate(numbers):
        t = -number
        if t not in targets:
            targets[t] = set()
        targets[t].add(index)

    for current_target in targets.keys():
        T = current_target
        # Generating b -> T - a map
        B_map: Dict[int, Set[int]] = {}
        for index, a in enumerate(numbers):
            if index in targets[T]:
                # skipping used indices
                continue

            b = T - a
            if b not in B_map:
                B_map[b] = set()
            B_map[b].add(index)

        # Finding b in numbers
        for b_index, b in enumerate(numbers):
            if b_index in used_indices:
                continue

            if b not in B_map:
                # No match for b
                continue

            if b_index in B_map[b] or b_index in targets[T]:
                # duplicate index: is in a or c (target)
                continue

            # Find first pair of unused indices for a, b, c
            c_indices = targets[T]
            a_indices = B_map[b]
            c_found: bool = False
            for c_index in c_indices:
                if c_index not in used_indices:
                    c_found = True
                    break

            a_found: bool = False
            for a_index in a_indices:
                if a_index not in used_indices:
                    a_found = True
                    break

            if c_found and a_found:
                triplets.append(sorted([a_index, b_index, c_index]))
                used_indices.add(a_index)
                used_indices.add(b_index)
                used_indices.add(c_index)

    return triplets


if __name__ == "__main__":
    # numbers: List[int] = [1, 2, 0, -1, -3, 1]
    # triplets = GetIndicesOfTripletsWithSumZero(numbers)
    # for triplet in triplets:
    #     print(triplet)

    numbers: List[int] = NUMBERS[: 36 * 3]
    triplets = GetIndicesOfTripletsWithSumZero(numbers)
    for triplet in sorted(triplets, key=lambda x: x[0]):
        print(
            triplet,
            f" --> {numbers[triplet[0]]:,} + {numbers[triplet[1]]:,} + {numbers[triplet[2]]:,} = {NUMBERS[triplet[0]] + NUMBERS[triplet[1]] + NUMBERS[triplet[2]]:,}",
        )
    print(f"Total numbers: {len(numbers):,}")
    print(f"Total triplets: {len(triplets):,}")

    used_indices: Set[int] = set()
    for triplet in sorted(triplets, key=lambda x: x[0]):
        if (
            triplet[0] in used_indices
            or triplet[1] in used_indices
            or triplet[2] in used_indices
        ):
            print(triplet)

        used_indices.add(triplet[0])
        used_indices.add(triplet[1])
        used_indices.add(triplet[2])
