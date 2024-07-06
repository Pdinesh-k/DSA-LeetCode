class Solution(object):
    def majorityElement(self, nums):
        length = len(nums)
        target = length/2
        setter = set()
        for num in nums:
            if(num not in setter):
                count = nums.count(num)
                if(count>target):
                    return num
                else:
                    setter.add(num)
        return -1
                    
            


                
        