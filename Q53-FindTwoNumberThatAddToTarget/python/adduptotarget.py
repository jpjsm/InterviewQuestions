from typing import List, Tuple


def Sum2NumbersToTargetSorted(l: List[int], t: int) -> List[Tuple[int, int]]:
    """Given 'l'a sorted list of integers, find all pairs that sum 't'

    Given that the list is sorted, we can say that
    -  a = l[i], b = l[j], where 0 <= i, j < len(l)
       and 'i' can be equal to 'j'.
    -  a + b == t, and a <= b

    - if b₀ < a₀ -> No solution possible
      •  l = [-3, -1, 0]
      •  t = -7
      •  a₀ = l[0] = -3
      •  b₀ = t - a₀ = -7 - (-3) = -4
         b₀ = -4, is outside the list and all other items in the list will
              require numbers farther out from the list

    - if bₙ₋₁ > aₙ₋₁ -> No solution possible
      •  l = [-3, -1, 0]
      •  t = 1
      •  aₙ₋₁ = l[n-1] = 0
      •  bₙ₋₁ = t - aₙ₋₁ = 1 - 0 = 1
         bₙ₋₁ = 1, is outside the list and all other items in the list will
              require numbers farther out from the list


    Args:
        l (List[int]): A sorted list of integers
        t (int): The target value of the sum of a pair of items from list

    Returns:
        List[Tuple[int,int]]: All pair of numbers from list that sum 't'
    """
    if (
        l is None
        or not isinstance(l, list)
        or len(l) < 1
        or not all(isinstance(x, int) for x in l)
    ):
        raise ValueError("'l' argument is an invalid list for this function")

    results: List[Tuple[int, int]] = []

    if len(l) == 1:
        return [(l[0], l[0])] if (l[0] + l[0]) == t else []

    last_item = len(l) - 1
    if (t - l[0] < l[0]) or (t - l[last_item] > l[last_item]):
        return results

    i = 0
    a = l[i]
    b = t - a
    bs = {}
    min_b = b
    while b >= a and i < last_item:
        bs[b] = a
        min_b = b
        i += 1
        a = l[i]
        b = t - a

    i = last_item
    b = l[i]
    while min_b <= b and i >= 0:
        if b in bs:
            results.append((bs[b], b))
            # If were searching for the first solution, return from here
            # with the pair
        i -= 1
        b = l[i]

    return results


def Sum2NumbersToTargetNotSorted(l: List[int], t: int) -> List[Tuple[int, int]]:
    if (
        l is None
        or not isinstance(l, list)
        or len(l) < 1
        or not all(isinstance(x, int) for x in l)
    ):
        raise ValueError("'l' argument is an invalid list for this function")

    results: List[Tuple[int, int]] = []

    bs = {}
    for a in l:
        b = t - a
        if a > b:
            continue
        bs[b] = a

    dedup = set()
    for b in l:
        if b in bs:
            a = bs[b]
            r = (a, b) if a < b else (b, a)
            # if r in dedup:
            #     continue
            dedup.add(r)
            results.append(r)

    return results


if __name__ == "__main__":
    test_lists = [
        ([0], 0, [(0, 0)]),
        ([-1, 0, 1], 0, [(-1, 1), (0, 0)]),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            10,
            [
                (1, 9),
                (2, 8),
                (3, 7),
                (4, 6),
                (5, 5),
            ],
        ),
        ([0, 1, 2], -1, []),
        ([0, 1, 2], 5, []),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            16,
            [
                (7, 9),
                (8, 8),
            ],
        ),
    ]

    for fun in [Sum2NumbersToTargetSorted, Sum2NumbersToTargetNotSorted]:
        for l, t, e in test_lists:
            expected = set(e)
            r = fun(l, t)
            if len(r) != len(e):
                print(
                    f"[{fun.__name__}({l}, {t})] Results length: {len(r)} is different than expected length: {len(e)}"
                )
            elif not all(r[i] in expected for i in range(len(r))):
                print(
                    f"[{fun.__name__}({l}, {t})] Results list {r} different than expected {e}"
                )
    print("Tests complete")
