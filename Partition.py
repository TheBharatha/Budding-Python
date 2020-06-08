import math
import os
import random
import re
import sys

def quickSort(arr):
    first = arr[0]
    left,right,equal = [],[],[]
    for i in arr:
        if i == first: 
            equal.append(i)
        elif i > first: 
            right.append(i)
        else: 
            left.append(i)
    allPiece = left + equal + right
    return(allPiece)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = quickSort(arr)
    print(' '.join(map(str, result)))
    print('\n')