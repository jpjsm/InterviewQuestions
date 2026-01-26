from fractions import Fraction
from typing import List, Set


def SumUnitFractions(l: int, target: int = 1) -> Set[int]:
    if not isinstance(l, int) or l < 3 or not isinstance(target, int) or target < 1:
        raise ValueError("Invalid arguments received.")

    result = [2, 3, 6]
    while len(result) < l:
        n = result.pop()
        n1 = n + 1
        nn = n * n1
        result.append(n1)
        result.append(nn)

    if target > 1:
        for i in range(l):
            result[i] *= target
    return set(result)


if __name__ == "__main__":
    tests = [
        ((3,), {2, 3, 6}),
        ((3, 7), {14, 21, 42}),
        ((5,), {2, 3, 7, 43, 1806}),
        ((4, 5), {10, 15, 35, 210}),
    ]

    for args, expected in tests:
        if len(args) == 2:
            l, t = args
        elif len(args) == 1:
            l, t = (args[0], 1)
        else:
            raise ValueError("Unexpected number of arguments!")

        r = SumUnitFractions(l, t)
        if r != expected:
            print(
                f"Sum of fractions SumUnitFractions({l},{t}): result {r} != {expected} expected"
            )
        R = sum([Fraction(1, d) for d in r])
        if Fraction(1, t) != R:
            print(f"Sum of fractions SumUnitFractions({l},{t}): {R} != {Fraction(1,t)}")

    print("Tests completed!")
