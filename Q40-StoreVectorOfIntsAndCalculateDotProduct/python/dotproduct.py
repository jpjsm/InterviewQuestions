from typing import Dict


def dotprod(a: Dict[int, float], b: Dict[int, float]) -> float:
    p = 0
    for a_key in a.keys():
        p += a[a_key] * b.get(a_key, 0.0)

    return p


if __name__ == "__main__":
    a = {1: 1.0, 2: 2, 4: 4, 6: 6}
    b = {0: 0.0, 3: 3, 6: 6, 9: 9}

    print(dotprod(a, b))
