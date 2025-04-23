class Solution(object):
    def uniquePaths(self, m, n):
        prev = [0 for _ in range(n)]
        for i in range(m):
            curr = [0 for _ in range(n)]
            for j in range(n):
                if i==0 and j==0:
                    curr[j]=1
                else:
                    up,left=0,0
                    if i>0:
                        up = prev[j]
                    if j>0:
                        left = curr[j-1]
                    curr[j] = up+left
            prev = curr
        return prev[n-1]
                
                
        