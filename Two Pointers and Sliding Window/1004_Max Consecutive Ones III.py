class Solution(object):
    def longestOnes(self, nums, k):
        zeroes = 0
        count = 0
        max_count = float("-inf")

        left,right=0,0

        while right<len(nums):
            if zeroes<=k:
                if nums[right]==1:
                    count+=1
                else:
                    zeroes+=1
                    count+=1
            else:
                count-=1
                max_count = max(max_count,count)
                while zeroes>k:
                    if nums[left]==0:
                        zeroes-=1
                    count-=nums[left]
                    left+=1
                right-=1
            right+=1
        if zeroes>k:
            max_count = max(max_count,count-1)
        else:
            max_count = max(max_count,count)
        return max_count





        





        
        