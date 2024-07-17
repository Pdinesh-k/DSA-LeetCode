class Solution(object):
    def generate(self, numRows):
        ls = []
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            dup_1 = [1],[1,1]
            ls.extend(dup_1)
            i = 1
            while(i < numRows-1):
                l = [1]
                for j in range(len(ls[i-1])):
                    l.append(ls[i][j] + ls[i][j+1])
                l.append(1)
                ls.append(l)
                i+=1
        return ls


        

        