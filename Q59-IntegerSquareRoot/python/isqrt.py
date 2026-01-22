def HighestBitOn(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError("Argument must be of integer type.")
    i = 0
    while n:
        n >>= 1
        i += 1
    return i


def iSqrt(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError("Argument must be of integer type.")

    if n < 0:
        raise ValueError("There are no square roots for negative numbers.")

    if n < 2:
        return n

    # Given N, there is S such S^2 = N; for all N > 0
    # => LOG2(S^2) = LOG2(N)
    #    2 * LOG2(S) = LOG2(N)
    #        LOG2(S) = LOG2(N)/2
    # The integer logarithm of N in base 2 is equal the the number of the
    # highest bit in N.
    # Divide that number by 2 and you have the logarithm lowest bound to search
    # for the square root of N. The logarithm highest bound is just adding 1 to
    # lowest bound.
    bit_len_half = n.bit_length() // 2
    left = 1 << (bit_len_half - 1)
    right = 1 << (bit_len_half + 1)
    while left < right:
        mid = (left + right) >> 1
        sq = mid * mid
        if sq == n:
            return mid
        if sq < n:
            left = mid + 1
        else:
            right = mid

    return left - 1


if __name__ == "__main__":
    tests = [
        (127, 11),
        (128, 11),
        (129, 11),
        (254, 15),
        (255, 15),
        (256, 16),
        (257, 16),
        (258, 16),
        (1022, 31),
        (1023, 31),
        (1024, 32),
        (1025, 32),
    ]

    for n, e in tests:
        r = iSqrt(n)
        if r != e:
            print(f"Wrong: iSqrt({n}) = {r}, expected {e}")

    print("Tests complete.")
