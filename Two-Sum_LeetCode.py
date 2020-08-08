class Solution:
    def twoSum(self, nums, target):
        if len(nums) == 2:
            return [0,1]
        else:
            for pos, value in enumerate(nums):
                diff = target - nums[pos]
                if diff in nums and pos != nums.index(diff):
                    return [pos, nums.index(diff)]
