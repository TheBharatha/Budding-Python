class Stick_count:
    def cutTheSticks(self, arr):
        arr.sort()
        uni_n = sorted(set(arr))
        self.logs = arr
        breaks = list(map(self.cut, uni_n))
        return(breaks)

    def cut(self, x):
        cuts = 0
        for i in range(len(self.logs)):
            if self.logs[i] >= x:
                cuts += 1
        return(cuts)

if __name__ == '__main__':
    n = int(input())
    kaddi = Stick_count()
    arr = list(map(int, input().rstrip().split()))
    result = kaddi.cutTheSticks(arr)
    print('\n'.join(map(str, result)))
    print('\n')
