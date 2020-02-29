import os
import sys

def solve(lowChar):
    propChar = ''
    for i in range(len(lowChar)-1):
        if i == 0:
            propChar = propChar + lowChar[i].upper() + lowChar[i+1]
        elif lowChar[i] == ' ':
            propChar = propChar + lowChar[i+1].upper()
        else:
            propChar = propChar + lowChar[i+1]
    return(propChar)

if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result + '\n')
