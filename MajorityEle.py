from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        givenArray = dict(Counter(nums))
        givenArray = [key  for (key, value) in givenArray.items() if value >= math.ceil(len(nums)/2)]
        return(givenArray[0])
