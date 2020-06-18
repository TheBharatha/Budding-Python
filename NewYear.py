import operator
a = [2,1,5,3,4]
b = sorted(a)
c = list(map(operator.sub, a, b))
c = list(map(str,c))
if '3' in c:
    print('Too chaotic')
else:
    c = list(filter(lambda  a: a>0, list(map(int,c))))
    c = sorted(set(c))
    print(sum(c))