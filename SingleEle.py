from collections import Counter
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        single = dict(Counter(nums))
        return(list(single.keys())[list(single.values()).index(1)])
