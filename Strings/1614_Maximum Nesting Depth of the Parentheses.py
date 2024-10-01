class Solution(object):
    def frequencySort(self, s):
        ls1 = []
        ls2 = []
        s = sorted(s)
        count = 1
        j = 0
        for i in range(0,len(s)):
            if i!=len(s)-1 and s[i] == s[i+1]:
                count+=1
            else:
                if count>1:
                    ls1.append((s[i],count))
                else:
                    ls2.append(s[i])
                count = 1
        ls1.sort(key=lambda x: -x[1])

        while j<len(ls1):
            char,curr = ls1[j]
            ls1[j] = char*curr
            j+=1

        string = "".join(ls1+ls2)
        return string
            

