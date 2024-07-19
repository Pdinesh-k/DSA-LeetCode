class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        count = 0
        i = 0
        while(True):
            if any(count>=len(s) for s in strs):
                break

            if all(strs[i][count] == strs[i+1][count] for i in range(len(strs)-1)):
                count+=1
            else:
                break 
        return strs[0][:count] if count>0 else "" 