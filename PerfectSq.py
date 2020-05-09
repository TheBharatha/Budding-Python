'''
Using math.sqrt()
'''
import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = str(math.sqrt(num))
        root = list(root.split('.'))
        if int(root[1]) > 0:
            return False
        else:
            return True

'''
Binary search
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lTree, rTree = 1, num
        while lTree < rTree:
            mid = (lTree + rTree) // 2
            if pow(mid,2) == num:
                return True
            elif num > pow(mid,2):
                lTree = mid + 1
            elif num < pow(mid,2):
                rTree = mid
        return False or num == 1
