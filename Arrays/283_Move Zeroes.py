class Solution(object):
    def rotate(self, nums, k):
        length = len(nums)
        k = k%length
        nums[:] = nums[length-k:] + nums[:length-k]

        



        