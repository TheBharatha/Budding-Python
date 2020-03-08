def pickingNumbers(a):
    b = list()
    tempSum = pairSum = 0
    a.sort(reverse=True)
    c = sorted(set(a),reverse=True)
    for sortNum in c:
        b.append([a.count(sortNum), sortNum])
    b.sort(key= lambda x:x[1], reverse=True)
    for left in b:
        for right in b:
            if abs(left[1] - right[1]) <= 1 and left != right:
                tempSum = left[0] + right[0]
                if tempSum > pairSum:
                    pairSum = tempSum
    if pairSum > max(b)[0]:
        return(pairSum)
    else:
        return(max(b)[0])
        
if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    print(str(result) + '\n')
