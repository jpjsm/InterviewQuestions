#!/usr/bin/env python3
import sys
import os.path

def integerdivisionreminder1(n, d):
    numerator = int(n)
    denominator = int(d)

    if denominator == 0:
        raise ZeroDivisionError

    if numerator == 0:
        return (0, denominator)

    n_sign = 1
    if numerator < 0:
        n_sign = -1
        numerator = numerator * n_sign

    d_sign = 1
    if denominator < 0:
        d_sign = -1
        denominator = denominator * d_sign

    if numerator < denominator:
        return (0, denominator)

    result = 0
    while numerator > denominator:
        result = result + 1
        numerator = numerator - denominator

    return (result * n_sign * d_sign, numerator)

def integerdivision1(n, d):
    numerator = int(n)
    denominator = int(d)

    (q, r) = integerdivisionreminder1(numerator, denominator)
    return q

def integerdivisionreminder2(n, d):
    numerator = int(n)
    denominator = int(d)

    if denominator == 0:
        raise ZeroDivisionError

    if numerator == 0:
        return (0, denominator)

    n_sign = 1
    if numerator < 0:
        n_sign = -1
        numerator = numerator * n_sign

    d_sign = 1
    if denominator < 0:
        d_sign = -1
        denominator = denominator * d_sign

    if numerator < denominator:
        return (0, denominator)

    q = 0
    while numerator > denominator:
        q2 = 1
        d2 = denominator
        while numerator > d2:
            d2 = d2 << 1
            q2 = q2 << 1

        d2 = d2 >> 1
        q2 = q2 >> 1
        numerator = numerator - d2
        q = q + q2

    return (q,numerator)
    
def integerdivision2(n, d):
    numerator = int(n)
    denominator = int(d)

    (q, r) = integerdivisionreminder2(numerator, denominator)
    return q

if __name__ == "__main__":
    import time
    import datetime
    numerator = 4000000000
    denominator = 7
    if len(sys.argv) > 2:
        numerator = sys.argv[1]
        denominator = sys.argv[2]

    start = datetime.datetime.now()
    print("{0} // {1} = {2}".format(numerator, denominator, integerdivisionreminder2(numerator, denominator)))
    delta = datetime.datetime.now() - start
    print("Elapsed time: {0}".format(str(delta)))
    start = datetime.datetime.now()
    print("{0} // {1} = {2}".format(numerator, denominator, integerdivisionreminder1(numerator, denominator)))
    delta = datetime.datetime.now() - start
    print("Elapsed time: {0}".format(str(delta)))
