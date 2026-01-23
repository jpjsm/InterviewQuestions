def ReverseInteger(n: int) -> int:
    isnegative = False
    if n < 0:
        n = -n
        isnegative = True

    return (-1 if isnegative else 1) * int(str(n)[::-1])


def ReverseInteger2(n: int) -> int:
    isnegative = False
    if n < 0:
        n = -n
        isnegative = True

    q, r = divmod(n, 10)
    R = r
    while q:
        q, r = divmod(q, 10)
        R *= 10
        R += r

    return (-1 if isnegative else 1) * R


if __name__ == "__main__":
    tests = [(123, 321), (1, 1), (0, 0), (98765, 56789), (-123, -321)]
    for n, e in tests:
        r = ReverseInteger(n)
        if r != e:
            print(f"[ReverseInteger] Houston we have a problem: {r} != {e}")
    for n, e in tests:
        r = ReverseInteger2(n)
        if r != e:
            print(f"[ReverseInteger2] Houston we have a problem: {r} != {e}")

    print("Tests completed")
