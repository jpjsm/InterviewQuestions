from typing import Dict, Set


def int2roman(n: int) -> str:
    if not isinstance(n, int) or n < 1 or n > 3999:
        raise ValueError(
            "'n' must be an integer number between 1 and 3,999; ends included."
        )

    N = n
    result = []
    while n >= 1000:
        n -= 1000
        result.append("M")

    if n >= 900:
        n -= 900
        result.append("CM")

    if n >= 500:
        n -= 500
        result.append("D")

    if n >= 400:
        n -= 400
        result.append("CD")

    while n >= 100:
        n -= 100
        result.append("C")

    if n >= 90:
        n -= 90
        result.append("XC")

    if n >= 50:
        n -= 50
        result.append("L")

    if n >= 40:
        n -= 40
        result.append("XL")

    while n >= 10:
        n -= 10
        result.append("X")

    if n == 9:
        n -= 9
        result.append("IX")

    if n >= 5:
        n -= 5
        result.append("V")

    if n == 4:
        n -= 4
        result.append("IV")

    while n:
        n -= 1
        result.append("I")

    if n != 0:
        raise ValueError(
            f"[ERROR] Conversion of N: {N} to Roman {"".join(result)} FAILED, there's a resifue of {n}"
        )
    return "".join(result)


def roman2int(r: str) -> int:
    validromanletters: Dict[str, int] = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    result = 0
    if not isinstance(r, str):
        raise ValueError("Invalid Roman numeral.")

    for i in range(len(r)):
        l = r[i]
        if l not in validromanletters:
            raise ValueError("Invalid Roman numeral.")
        n = validromanletters[l]
        if i + 1 < len(r) and n < validromanletters[r[i + 1]]:
            n = -n
        result += n
    return result


if __name__ == "__main__":
    tests = [
        (19, "XIX"),
        (39, "XXXIX"),
        (49, "XLIX"),
        (246, "CCXLVI"),
        (789, "DCCLXXXIX"),
        (2421, "MMCDXXI"),
        (160, "CLX"),
        (207, "CCVII"),
        (1009, "MIX"),
        (1066, "MLXVI"),
        (3999, "MMMCMXCIX"),
    ]

    for n, e in tests:
        r = int2roman(n)
        print(f"{n} -> {r}")
        if e != r:
            print(f"[ERROR] Failed 'int2roman({n})': {r} != {e} expected")

    for e, n in tests:
        r = roman2int(n)
        print(f"{n} -> {r}")
        if e != r:
            print(f"[ERROR] Failed 'roman2int({n})': {r} != {e} expected")

    print("Tests Completed")
