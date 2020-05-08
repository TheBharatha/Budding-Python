class Solution:
    def checkStraightLine(self, coordinates):
        slope = list()
        for xy in range(1,len(coordinates)):
            pairOne = coordinates[xy]
            pairTwo = coordinates[xy-1]
            try:
                slope.append(abs((pairTwo[1] - pairOne[1]) / (pairTwo[0] - pairOne[0])))
            except:
                slope.append(0.0)
        print(slope)
        if len(set(slope)) == 1:
            return True
        else:
            return False

if __name__ == "__main__":
    line = Solution()
    print(line.checkStraightLine([[-1,1],[-6,-4],[-6,2],[2,0],[-1,-2],[0,-4]]))