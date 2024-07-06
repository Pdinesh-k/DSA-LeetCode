class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
       max_count , cur_count = -1,0
       for i in range(0,len(nums)):
            if nums[i] == 1:
                cur_count+=1
            else:
                max_count = max(cur_count,max_count)
                cur_count = 0
       return max(max_count,cur_count)
        