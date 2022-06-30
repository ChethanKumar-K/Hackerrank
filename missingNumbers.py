#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#

def missingNumbers(arr, brr):
    # Write your code here
    answer = []
    dic1 = {}
    dic2 = {}
    for i in arr:
        dic1[i] = 0
    for j in brr:
        dic2[j] = 0
    for i in arr:
        dic1[i] += 1
    for j in brr:
        dic2[j] += 1
    for k in dic2:
        try:
            if(dic2[k] != dic1[k]):
                answer.append(k)
        except:
            answer.append(k)
    answer.sort()    
    return(answer)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
