class Solution(object):
    def threeSum(self, nums):
        length = len(nums)
        ls=[]
        nums.sort()
        for i in range(length-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left,right=i+1,length-1
            
            while left<right:
                total = nums[i]+nums[left]+nums[right]
                if total==0:
                    temp = [nums[i],nums[left],nums[right]]
                    ls.append(temp)

                    while left<right and nums[left] == nums[left+1]:
                        left+=1
                    while left < right and nums[right] == nums[right-1]:
                        right-=1
                    
                    left+=1
                    right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1
        return ls
            

            

        