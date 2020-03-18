def angryProfessor(k, a):
    a = sorted(a)
    result = list(map(cancel,a))
    if sum(result) >= k:
        return('NO')
    else:
        return('YES')

def cancel(x):
    if x <= 0:
        return(1)
    else:
        return(0)

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])
        a = list(map(int, input().rstrip().split()))
        result = angryProfessor(k, a)
        print(result + '\n')
