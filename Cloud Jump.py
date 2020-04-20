#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = cross = 0
    for clouds in range(len(c)-1):
        if c[clouds] == 0:
            jumps += 1
            if jumps%2 == 0:
                cross += 1
                jumps = 0
    if len(c)%2 == 0:
        return(cross-1)
    else:
        return(cross)

if __name__ == '__main__':

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(str(result) + '\n')