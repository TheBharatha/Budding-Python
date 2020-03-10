def appendAndDelete(s, t, k):
    given = list(s)
    sLen = len(given)
    target = list(t)
    tLen = len(target)
    ops = 0
    if sLen > tLen:
        while sLen != 0:
            try:
                if given[sLen-1] == target[sLen-1]:
                    ops = ops
                    sLen -= 1
                else:
                    ops += 2
                    sLen -= 1
            except:
                ops += 1
                given.pop()
                sLen = len(given)
    elif  sLen < tLen:
        while tLen != 0:
            try:
                if target[tLen-1] == given[tLen-1]:
                    ops = ops
                    tLen -= 1
                else:
                    ops += 2
                    tLen -= 1
            except:
                ops += 1
                tLen -= 1
    elif sLen == tLen:
        start = 0
        while start != sLen:
            if target[start] == given[start]:
                ops = ops
                start += 1
            else:
                ops = len(given[start:]) * 2
                start = sLen
        if ops > k:
            return('No')
        else:
            return('Yes')
    
    if k%2 != 0 and ops%2 != 0 or k%2 != 0 and ops%2 == 0 or ops%2 == 0:
        return('Yes')
    elif k%2 == 0 and ops%2 != 0 or k%2 == 0 and ops%2 == 0:
        return('No')

if __name__ == '__main__':
    s = 'asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv'
    t = 'bsdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv'
    k = 100
    result = appendAndDelete(s, t, k)
    print(result)
