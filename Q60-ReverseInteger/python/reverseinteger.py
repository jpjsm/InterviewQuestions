def ReverseInteger(n: int) -> int:
    return int(str(n)[::-1])


def ReverseInteger2(n: int) -> int:
    q, r = divmod(n, 10)
    R = r
    while q:
        q, r = divmod(q, 10)
        R *= 10
        R += r

    return R


if __name__ == "__main__":
    tests = [(123, 321), (1, 1), (0, 0), (98765, 56789)]
    for n, e in tests:
        r = ReverseInteger(n)
        if r != e:
            print(f"[ReverseInteger] Houston we have a problem: {r} != {e}")
    for n, e in tests:
        r = ReverseInteger2(n)
        if r != e:
            print(f"[ReverseInteger2] Houston we have a problem: {r} != {e}")

    print("Tests completed")
