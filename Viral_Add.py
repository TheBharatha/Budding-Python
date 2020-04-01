import math

def viralAdvertising(n):
    m = 5
    cum = list()
    for start in range(1, n+1):
        cum.append(math.floor(m/2))
        m = cum[start-1] * 3
    return(sum(cum))

if __name__ == '__main__':
    n = int(input())
    result = viralAdvertising(n)
    print(str(result) + '\n')
