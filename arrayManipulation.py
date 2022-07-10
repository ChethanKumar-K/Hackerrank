#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

###       MAIN  LOGIC     ###

def arrayManipulation(n, queries):
    # Write your code here
    arr=[]    
    for i in range(n+1):
        arr.append(0)
    for i in range(len(queries)):
        start = queries[i][0]
        end = queries[i][1]
        addElem = queries[i][2]
        arr[start] += addElem
        if((end+1)<=n):
            arr[end+1] -= addElem
    sum =0
    maxSum = 0
    for j in range(0,n+1):
        sum = sum+arr[j]
        maxSum = max(maxSum,sum)
    return(maxSum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
