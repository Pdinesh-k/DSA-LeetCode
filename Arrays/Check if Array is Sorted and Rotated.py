class Solution(object):
    def check(self, nums):
        if not nums:
            return False
        arr = []
        arr1 = []
        prev = nums[0]
        arr.append(nums[0])
        flag = False
        for i in range(1,len(nums)):
            if flag == False:
                if nums[i] >= prev:
                    arr.append(nums[i])
                else:
                    arr1.append(nums[i])
                    flag = True
            else:
                arr1.append(nums[i])
                flag = True
            prev = nums[i]
        if sorted(nums) == arr1+arr:
            return True
        else:
            return False



        