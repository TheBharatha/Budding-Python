import math
import os
import re
import sys

def diagonalDifference(arr):
    mag_num = len(arr)
    left = list()
    right = list()
    for i in range(mag_num):
        left.append(arr[i][i])
        right.append(arr[i][(mag_num-1)-i])
    if not mag_num%2 == 0:
        rep = mag_num//2
        del(left[rep])
    return(abs(sum(left)-sum(right)))

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(str(result) + '\n')
