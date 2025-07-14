#!/usr/bin/env python3
import sys
import os.path

DebugMode = False
CacheEnabled = True
ParenthesesGroups = {}

def generatebalancedparentheses(n:int):
    if n < 0:
        raise ArithmeticError("Argument '{0}' must be greater or equal to zero".format(n))

    if n == 0:
        return ['']

    if n == 1:
        return ['()']

    if CacheEnabled and n in ParenthesesGroups:
        return ParenthesesGroups[n]

    result = []
    for i in range(0,n):
        for l in generatebalancedparentheses(i):
            for r in generatebalancedparentheses(n - 1 - i):
                s = '(' + l + ')' + r
                result.append(s)
        
    if CacheEnabled: 
        ParenthesesGroups[n] = result
    
    return result

if __name__ == "__main__":
    n = 16
    if len(sys.argv) > 1:
        n1 = int(sys.argv[1])
        if n1 >= 0:
            n = n1

    for i in range(0,n):
        print("{0:2} => {1}".format(i,len(generatebalancedparentheses(i))))
