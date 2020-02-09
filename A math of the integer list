# No multiplication required. All the multiples are present in the initial list created. 
# All that is needed is to get the values from the relevant index.

def expose(n):
    raw = list()
    dist = 0
    for i in range(2,n+1):
        raw.append(i)
    start = raw[dist]
    while start != n:
        print('Block start')
        for j in range(dist,len(raw),start):
            print(raw[j])
        print('Block end. \n')
        dist += 1
        start = raw[dist]
                    
if __name__ == '__main__':
    n = int(input())
    expose(n)
