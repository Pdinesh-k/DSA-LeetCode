class Solution(object):
    def minFallingPathSum(self, matrix):
        m,n=len(matrix),len(matrix[0])
        prev = []
        i = m-1
        for j in range(0,n):
            prev.append(matrix[i][j])
        
        for i in range(m-2,-1,-1):
            curr = [0 for j in range(n)]
            for j in range(0,n):
                down = prev[j]
                down_left = prev[j-1] if j-1>=0 else float("inf")
                down_right = prev[j+1] if j+1<n else float("inf")
                curr[j] = matrix[i][j]+min(down,down_left,down_right)
            prev = curr

        return min(prev)
                

                


        