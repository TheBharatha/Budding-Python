class Movie:
    def beautifulDays(self, i, j, k):
        self.dinominator = k
        rangeNums = list(range(i, j+1))
        nums = list(map(self.check, rangeNums))
        return(sum(nums))

    def check(self, day):
        beauty = day - int(str(day)[len(str(day))::-1])
        if beauty%self.dinominator == 0:
            return 1
        else:
            return 0

if __name__ == '__main__':
    ijk = input().split()
    i = int(ijk[0])
    j = int(ijk[1])
    k = int(ijk[2])
    objMovie = Movie()
    result = objMovie.beautifulDays(i, j, k)
    print(str(result) + '\n')
