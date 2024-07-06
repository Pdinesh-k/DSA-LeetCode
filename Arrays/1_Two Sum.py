class Solution(object):
    def minSubArrayLen(self, target, nums):
        length = len(nums)
        left = 0
        current_sum = 0
        minimal_length = float('inf')

        for right in range(length):

            current_sum+=nums[right]

            while(current_sum>=target):
                minimal_length = min(minimal_length,right-left+1)
                current_sum-=nums[left]
                left+=1
        return minimal_length if minimal_length !=float('inf') else 0








                




        