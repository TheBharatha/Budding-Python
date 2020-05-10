class Solution:
    def findJudge(self, N, trust):
        judgeAddress = dict()
        zeroIndex = list(map(lambda x: x[0], trust))
        oneIndex = list(map(lambda y: y[1], trust))
        for person in range(1,N+1):
            judgeAddress[person] = [zeroIndex.count(person), oneIndex.count(person)]
            print(judgeAddress)
            try:
                return(list(judgeAddress.keys())[list(judgeAddress.values()).index([0,N-1])])
            except ValueError:
                pass

        



if __name__ == "__main__":
    N = int(input('Enter the number of people: '))
    trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    callJudge = Solution()
    print(callJudge.findJudge(N,trust))