class Solution(object):
    def findMin(self, nums):
        start = 0
        end = len(nums)-1

        while (start<=end):
            mid = (start+end)//2

            if nums[mid]<nums[end]:
                end = mid
            else:
                start = mid+1
        return nums[end]
        