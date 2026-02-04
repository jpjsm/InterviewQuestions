from math import isqrt


def is_prime(n: int) -> bool:
    if not isinstance(n, int):
        raise ValueError("Argument 'n' must be an integer.")
    n = abs(n)
    if n < 2:
        return False

    if n in (2, 3):
        return True

    # check multiples of 2 and 3
    if n % 2 == 0 or n % 3 == 0:
        return False

    isqrt_n = isqrt(n)  # Highest value to test

    # Sieving by: p = 6 * i ± 1
    i = 5

    while i <= isqrt_n:
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i += 6

    return True


def prime_floor(n: int) -> int:

    if not isinstance(n, int):
        raise ValueError("Argument 'n' must be an integer.")

    if n == 1 or n == 0 or n == -1:
        return -2

    while not is_prime(n):
        n -= 1

    return n


if __name__ == "__main__":
    print("Start 'is_prime' tests.")
    is_prime_tests = [
        (7, True),
        (9, False),
        (11, True),
        (13, True),
        (17, True),
        (19, True),
        (21, False),
        (99, False),
        (101, True),
        (3917, True),
        (3919, True),
        (3921, False),
        (7891, False),
        (7901, True),
        (7903, False),
        (7919, True),
    ]

    for n, expected in is_prime_tests:
        actual = is_prime(n)
        if actual != expected:
            print(f"is_prime({n}) result {actual} != {expected} expected.")

    print("'is_prime' tests complete.")

    print("Start 'prime_floor' tests.")
    floor_prime_tests = [
        (7, 7),
        (9, 7),
        (19, 19),
        (21, 19),
        (99, 97),
        (101, 101),
        (1090, 1087),
        (1708, 1699),
        (7063, 7057),
        (7891, 7883),
        (7901, 7901),
        (7903, 7901),
        (2147483643, 2147483629),
        (2147483647, 2147483647),
        (4294967296, 4294967291),
        (-2, -2),
        (-4, -5),
        (-4294967281, -4294967291),
    ]

    for n, expected in floor_prime_tests:
        actual = prime_floor(n)
        if actual != expected:
            print(f"prime_floor({n}) result {actual} != {expected} expected.")

    print("'prime_floor' tests complete.")
