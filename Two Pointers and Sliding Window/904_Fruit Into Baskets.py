class Solution(object):
    def totalFruit(self, fruits):
        left,right = 0,0
        max_len = float("-inf")
        _dict = {}

        while right<len(fruits):
            if fruits[right] in _dict:
                _dict[fruits[right]]+=1
            else:
                _dict[fruits[right]] = 1
            
            while len(_dict)>2:
                _dict[fruits[left]]-=1
                
                if _dict[fruits[left]]==0:
                    del _dict[fruits[left]]
                left+=1
            max_len = max(max_len,right-left+1)
            right+=1
        return max_len








            
            


            


        