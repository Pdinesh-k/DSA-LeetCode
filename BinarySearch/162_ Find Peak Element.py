class Solution(object):

    def __init__(self):
        self.num = float("inf")

    def checker(self,threshold,bloomDay,m,k):
        counter = 0
        bouq = 0
        for i in range(0,len(bloomDay)):
            if bloomDay[i]<=threshold:
                counter+=1
            else:
                bouq+=counter//k
                counter = 0

            if bouq>=m:
                return True  

        bouq+=counter//k
        return bouq>=m
        

    def minDays(self, bloomDay, m, k):

        length = len(bloomDay)
        if m*k > length:
            return -1
        
        _min = min(bloomDay)
        _max = max(bloomDay)

        start,end = _min,_max

        while(start<=end):
            
            mid = (start+end)//2

            res = self.checker(mid,bloomDay,m,k)

            if res:
                self.num = min(self.num,mid)
                end = mid-1
            else:
                start=mid+1
        return self.num if self.num!=float("inf") else -1




        


        