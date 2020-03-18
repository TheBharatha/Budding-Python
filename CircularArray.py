def circularArrayRotation(a, k, queries):
    result = list()
    for _ in range(k):
        a.insert(0,a.pop())
    for i in queries:
        result.append(a[i])
    return(result)

if __name__ == '__main__':
    nkq = input().split()
    n = int(nkq[0])
    k = int(nkq[1])
    q = int(nkq[2])
    a = list(map(int, input().rstrip().split()))
    queries = []
    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)
    result = circularArrayRotation(a, k, queries)
    print('\n'.join(map(str, result)))
    print('\n')
