import math
import os
import random
import re
import sys

def permutationEquation(p):
    ranges = list(range(1,len(p)+1))
    sequence = list()
    for indexs in ranges:
        sequence.append(p.index(p.index(indexs)+1)+1)
    return(sequence)

if __name__ == '__main__':
    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    print('\n'.join(map(str, result)))
    print('\n')
