#!/usr/bin/env python3

def fib(i):
    n = int(i)
    if n < 0:
        raise ValueError('Argument/parameter must be positive')
    if n == 0:
        return 0

    f0 = int(0)

    if n == 1:
        return 1

    f1 = int(1)

    n -= 1
    while n > 0:
        f2 = f0 + f1
        f0 = f1
        f1 = f2
        n -= 1

    return f2

def KthFibStr(m,j):
    n = int(m)
    k = int(j)

    if m < 0 or k < 0:
        raise ValueError('Argument/parameter must be positive')

    if k > fib(n+2):
        raise IndexError("Value of 'j' out of range")

    if n == 0:
        return 'a'

    if n == 1:
        if k == 0:
            return 'b'
        
        return 'c'

    if k < fib(n):
        return KthFibStr(n-2,k)

    return KthFibStr(n-1, k-fib(n))


if (__name__ == "__main__"):
    print("... starting ...")

    for i in range(0,51):
        print("{0:4} {1:24,}".format(i, fib(i)))

    for n in range(0,7):
        for k in range(0, fib(n+2)):
            print("KthFibStr({0},{1}) = {2}".format(n,k,KthFibStr(n,k)))

    print("KthFibStr({0},{1}) = {2}".format(50, 133,KthFibStr(50,133)))
    