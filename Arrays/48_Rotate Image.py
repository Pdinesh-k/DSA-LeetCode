class Solution(object):
    def setZeroes(self, matrix):
        a,b= len(matrix),len(matrix[0])
        row_zero = [0]*a
        col_zero = [0]*b
        for i in range(a):
            for j in range(b):
                if matrix[i][j] == 0:
                    row_zero[i] = 1
                    col_zero[j] = 1
        
        for i in range(a):
            for j in range(b):
                if row_zero[i] or col_zero[j] == 1:
                    matrix[i][j] = 0
        return matrix

        