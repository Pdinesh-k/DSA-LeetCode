class Solution(object):
    def smallestDivisor(self,nums,threshold):
        start = 1
        end = max(nums)
        min_num = end

        while(start<=end):
            divisor_sum = 0

            mid = (start+end)//2

            for i in range(0,len(nums)):
                divisor_sum+=(nums[i]+mid-1)//mid
            
            if divisor_sum>threshold:
                start = mid+1
            else:
                min_num = min(min_num,mid)
                end = mid-1
        return min_num






        