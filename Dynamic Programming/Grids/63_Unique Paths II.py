class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        n,m = len(obstacleGrid[0]),len(obstacleGrid)
        prev = [0 for _ in range(n)]
        for i in range(m-1,-1,-1):
            cur = [0 for _ in range(n)]
            for j in range(n-1,-1,-1):
                if obstacleGrid[i][j] == 1:
                    cur[j] = 0
                elif i==m-1 and j==n-1:
                    cur[j]=1
                else:
                    right,down=0,0
                    if i<m-1:
                        down = prev[j]
                    if j<n-1:
                        right = cur[j+1]
                    cur[j] = down+right
            prev = cur
        return prev[0]
                
        