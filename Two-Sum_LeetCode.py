class Solution:
    def twoSum(self, nums, target):
        for pos, value in enumerate(nums):
            diff = target - nums[pos]
            if diff in nums and pos != nums.index(diff):
                return [pos, nums.index(diff)]
