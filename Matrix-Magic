import math
import os
import sys

def diagonalDifference(arr):
    mag_num = len(arr)
    for i in range(mag_num):
        print(arr[i][i])
    
    for j in range(mag_num):
        for k in range(mag_num-1,0,-1):
            print(arr[j][k])

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    diagonalDifference(arr)
