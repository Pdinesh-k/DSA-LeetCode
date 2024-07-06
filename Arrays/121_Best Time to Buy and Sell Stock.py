class Solution(object):
    def maxSubArray(self, nums):
        if not nums:
            return nums
        length = len(nums)
        if length == 1:
            return nums[0]
        maximum = float("-inf")
        sum = 0
        for i in range(len(nums)):
            sum+=nums[i]
            maximum = max(sum,maximum)
            if sum<0:
                sum = 0
        return maximum



        