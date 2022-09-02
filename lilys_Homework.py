#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def lilysHomework(arr):
    # Write your code here
    
    def minSorts(arr):
        #dictionary to keep track of indices
        idx = {}
        
        for i in range(len(arr)):
            idx[arr[i]] = i
            
        #creating a sorted array 
        sortedarr = sorted(arr)
        
        #count variable to keep track of no of swaps
        count = 0
        
        for i in range(len(arr)):
            if(arr[i] != sortedarr[i]):
                count += 1
                
                #get the index of the element to be swapped
                swap_idx = idx[sortedarr[i]]
                
                #update the idx dictionary to new value
                idx[arr[i]] = swap_idx
                idx[sortedarr[i]] = i
                
                #perform the swap
                arr[i] , arr[swap_idx] = arr[swap_idx],arr[i]
                
        print(arr)
        print(idx)
        return(count)
                
    normalOrder = minSorts(arr[::])
    reverseOrder = minSorts(arr[::-1])
    
    return(min(normalOrder,reverseOrder))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
