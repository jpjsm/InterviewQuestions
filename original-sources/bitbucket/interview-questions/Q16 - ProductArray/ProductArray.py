#!/usr/bin/env python3

'''
    Given an array arr[] of n integers, construct a Product Array prod[] (of same size) 
    such that prod[i] is equal to the product of all the elements of arr[] except arr[i].

    Note: 
    As an extended interview question
    Solve it without division operator and in O(n).
'''

def ProdArray1(arr):
    P = 1
    for p in arr:
        P *= p

    return [P//p for p in arr]

def ProdArray2(arr):
    alen = len(arr)
    results = [1] * alen
    right = [0] * alen
    left = [0] * alen
    for i in range(1,alen):
        left[i-1] = arr[i-1] * (left[i-2] if i > 1 else 1)
        right[alen-i] = arr[alen-i] * (right[alen + 1 - i] if i > 1 else 1)
    
    for i in range(0,alen):
        results[i] = (left[i-1] if i > 0 else 1) *(right[i + 1] if i < alen -1 else 1)

    return results


if __name__ == "__main__":
    print("... starting {0}".format(__file__))
    TestCases =[
        [1, 2, 3, 4, 5, 6],
        [-1, 2, -3, 4, -5, 6],
        [1, 1, 1, 1, 1, 1],
    ]

    ExpectedResults =[
        [720, 360, 240, 180, 144, 120],
        [720, -360, 240, -180, 144, -120],
        [1, 1, 1, 1, 1, 1],
    ]
    for i in range(0, len(TestCases)):
        TestResults1 = ProdArray1(TestCases[i])
        TestResults2 = ProdArray2(TestCases[i])
        for j in range(0, len(TestCases[i])):
            assert TestResults1[j] == ExpectedResults[i][j], "ProdArray1 failed to produce expected results: {0} =! {1}, for i:={2} and j:={3}".format(TestResults1, ExpectedResults[i], i, j)
            assert TestResults2[j] == ExpectedResults[i][j], "ProdArray2 failed to produce expected results: {0} =! {1}, for i:={2} and j:={3}".format(TestResults2, ExpectedResults[i], i, j)

    print("Function tests completed successfully.")