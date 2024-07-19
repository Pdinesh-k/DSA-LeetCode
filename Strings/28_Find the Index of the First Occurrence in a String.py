class Solution(object):
    def convert(self, s, numRows):
        if numRows > len(s) or numRows==1:
            return s

        rows = [[] for i in range(numRows)]
        index = 0
        step = -1
        for i in s:
            rows[index].append(i)
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            index+=step
        for i in range(numRows):
            rows[i] = "".join(rows[i])
        return "".join(rows)
            

        