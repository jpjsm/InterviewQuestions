#!/usr/bin/env python3

SumsOfN = {}
SumsOfN[0] = []
SumsOfN[1] = [[1]]


def GenerateSumsOfN(N):
    n = int(N)
    if n in SumsOfN:
        return SumsOfN[n]

    results = [[n]]
    duplicate_check = set()
    for i in range(1, n):
        for r in GenerateSumsOfN(i):
            if len(r) == 1:
                c = [r[0], n - i]
            else:
                c = r + [n - i]

            check = "_".join([str(x) for x in sorted(c)])
            if check not in duplicate_check:
                results += [r + [n - i]]
                duplicate_check.add(check)

    if n not in SumsOfN:
        SumsOfN[n] = results

    return results


if __name__ == "__main__":
    print("... starting ...")
    n = 6

    results = GenerateSumsOfN(n)
    rs = []

    for r in results:
        rs.append(sorted(r, reverse=True))

    for r in sorted(rs, reverse=True):
        print(" + ".join([str(x) for x in r]))
    print("... done ...")
