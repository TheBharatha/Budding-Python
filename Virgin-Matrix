import os
import random
import re
import sys
import numpy as np

def VirginSquare(sq):
    host = np.zeros(shape=(3,3))
    missing = list()
    index = list()
    
    r = 0
    d = 1
    c = 2
    
    if s[r][r] % 2 != 0:
        s[r][r] = 0
    elif s[r][c] %2 != 0:
        s[r][c] = 0
    elif s[c][r] %2 != 0:
        s[c][r] = 0
    elif s[c][c] %2 != 0:
        s[c][c] = 0
    
    if s[r][d] % 2 == 0:
        s[r][d] = 0
    elif s[d][r] % 2 == 0:
        s[d][r] = 0
    elif s[d][d] != 5:
        s[d][d] = 5
    elif s[d][c] % 2 == 0:
        s[d][c] = 0
    elif s[c][d] % 2 == 0:
        s[c][d] = 0
    
    for i in range(len(s)):
        for j in range(len(s)):
            if any(s[i][j] in x for x in host):
                host[i][j] = 0
                index.append(i)
                index.append(j)
            else:
                host[i][j] = s[i][j]
    
    for i in range(1,10):
        if not any(i in x for x in host):
            if i%2 != 0:
                missing.append(i)
            else:
                missing.append(i)
    
    if len(index) == 2:
        host[index[0]][index[1]] = missing[0]
            
    print(host)
    print(missing)
    print(index)


if __name__ == '__main__':
    sq = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))
    VirginSquare(sq)
