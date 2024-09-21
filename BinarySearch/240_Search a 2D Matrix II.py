class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        row = 0
        column = m-1

        while(row<n and column>=0):
            if matrix[row][column] == target:
                return True
            elif matrix[row][column]<target:
                row+=1
            else:
                column-=1
        return False
        