class Solution(object):
    def rearrangeArray(self, nums):
        arr = [0]*len(nums)
        pos,neg = 0,1
        for i in range(0,len(nums)):
            if nums[i]>0:
                arr[pos] = nums[i]
                pos+=2
            else:
                arr[neg] = nums[i]
                neg+=2
        return arr