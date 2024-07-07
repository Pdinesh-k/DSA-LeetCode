class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums[:] = sorted(nums)
        max_streak = 1
        cur_streak = 1
        for i in range(0,len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                cur_streak+=1
            elif nums[i] == nums[i+1]:
                continue
            else:
                max_streak = max(max_streak,(cur_streak))
                cur_streak = 1
        max_streak = max(max_streak,cur_streak)

            
        return max_streak       