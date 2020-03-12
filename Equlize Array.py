import math
import os
import random
import re
import sys

class Equilize:
    def equalizeArray(self,arr,n):
        arr.sort()
        self.brr = arr
        self.uni_arr = sorted(set(arr))
        uni_count = list(map(self.countEqual,self.uni_arr))
        return(n - max(uni_count))
    
    def countEqual(self, x):
        return(self.brr.count(x))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    seq = Equilize()
    result = seq.equalizeArray(arr,n)
    print(str(result) + '\n')
    fptr.close()
