class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        jewel_set = set(jewels)
        count = 0
        
        for i in stones:
            if i in jewel_set:
                count += 1
                
        return count


        