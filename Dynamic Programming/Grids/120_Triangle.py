class Solution(object):
    def minimumTotal(self, triangle):
        n = len(triangle)
        front = [0 for _ in range(n)]

        for j in range(0,len(triangle)):
            front[j] = triangle[n-1][j]

        for i in range(n-2,-1,-1):
            cur = [0 for _ in range(i+1)]
            for j in range(i,-1,-1):
                down = triangle[i][j]+front[j]
                down_right = triangle[i][j]+front[j+1]
                cur[j] = min(down,down_right)
            front = cur

        return front[0]


        