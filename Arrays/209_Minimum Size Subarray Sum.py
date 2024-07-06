class Solution(object):
    def singleNumber(self, nums):
        xor = 0
        for i in range(len(nums)):
            xor = xor^nums[i]
        return xor
        