class Distance:
    def minimumDistances(self, a):
        unique = list(set(a))
        self.a = a
        self.multipleItems = list(filter(lambda x: a.count(x) > 1, unique))
        if len(self.multipleItems) < 1:
            return(-1)
        else:
            distences = list(map(self.checkDistance, self.multipleItems))
            return(min(distences))
    
    def checkDistance(self, element):
        start = self.a.index(element)
        begin = start
        for item in range(start+1, len(self.a)):
            if self.a[item] == element:
                spaces = item - begin
                begin = item
                return(spaces)

if __name__ == '__main__':

    n = int(input())

    a = list(map(int, input().rstrip().split()))
    
    arrayDistance = Distance()

    result = arrayDistance.minimumDistances(a)

    print(str(result) + '\n')