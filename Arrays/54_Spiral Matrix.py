class Solution(object):
    def spiralOrder(self, matrix):
        l = []
        while matrix:
            if matrix:
                l+=matrix.pop(0)
            if matrix and matrix[0]:
                for i in matrix:
                    l.append(i.pop())
            if matrix:
                l+=matrix.pop()[::-1]
            if matrix and matrix[0]:
                for i in matrix[::-1]:
                    l.append(i.pop(0))
        return l


        