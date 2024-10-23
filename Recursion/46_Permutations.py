class Solution(object):
    def recursion(self,sub,nums,ls):
        if len(nums) == 0:
            ls.append(sub)
            return
        
        ch = nums[0]

        for i in range(0,len(sub)+1):
            first = sub[:i]
            second = sub[i:]
            self.recursion(first+[ch]+second,nums[1:],ls)
            
    def permute(self, nums):
        ls = []
        self.recursion([],nums,ls)
        return ls


        