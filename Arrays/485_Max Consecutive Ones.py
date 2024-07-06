class Solution(object):
    def missingNumber(self, nums):
        length = len(nums)
        sum = 0
        for i in range(0,length):
            sum+=nums[i]
        formula = (length*(length+1))/2
        return formula-sum



        