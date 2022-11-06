#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'substrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING n as parameter.
#

def substrings(n):
    # Write your code here
    result = 0
    weights = [] # to store powers of 10 i.e, 100 10 1
    values = []   # to store weights i.e, 111 11 1
    mod = (math.pow(10,9) + 7)
    weights.append(1)
    values.append(1)
    for i in range(1,len(n)):
        values.append((values[i-1]*10)%mod)
        weights.append((weights[i-1]+values[i])%mod)
    
    for i in range(len(n)):
        result += (int(n[i]) * weights[len(n) - i - 1] * (i + 1))%mod
    return (int(result%mod))
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()
