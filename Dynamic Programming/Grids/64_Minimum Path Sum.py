class Solution(object):
    def minPathSum(self, grid):
        m,n=len(grid),len(grid[0])
        prev = [0 for _ in range(n)]
        for i in range(m-1,-1,-1):
            cur = [0 for _ in range(n)]
            for j in range(n-1,-1,-1):
                i_last,j_last = float("inf"),float("inf")
                if i==m-1 and j==n-1:
                     cur[j] = grid[i][j]
                else:
                    if i<m-1:
                        i_last = prev[j]
                    if j<n-1:
                        j_last = cur[j+1]
                    cur[j] = grid[i][j]+min(i_last,j_last)
            prev = cur
        return prev[0]