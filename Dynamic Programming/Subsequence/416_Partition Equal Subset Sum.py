class Solution(object):
    def dp_subsequence(self,nums,sum_,target):
        prev = [False]*(target+1)
        curr = [False]*(target+1)
        prev[0] = curr[0] = True
        if nums[0]<=target:
            prev[nums[0]] = True
        for i in range(1,len(nums)):
            for target_ in range(1,target+1):
                not_take = prev[target_]
                take = False
                if nums[i]<=target_:
                    take = prev[target_-nums[i]]
                curr[target_] = take or not_take
            prev = curr[:]
        return prev[target]


    def canPartition(self, nums):
        total_sum = sum(nums)
        target = total_sum//2
        sum_ = 0
        if total_sum%2!=0:
            return False
        return self.dp_subsequence(nums,sum_,target)
