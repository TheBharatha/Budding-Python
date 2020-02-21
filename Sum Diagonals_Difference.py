import math
import os
import sys

def diagonalDifference(arr):
    mag_num = len(arr)
    sum1 = sum2 = 0
    for i in range(mag_num):
        sum1 = sum1 + arr[i][i]
        sum2 = sum2 + arr[i][(mag_num-1)-i]
    return(abs(sum1-sum2))

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(str(result) + '\n')
