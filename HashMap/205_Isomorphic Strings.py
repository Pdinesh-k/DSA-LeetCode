class Solution(object):
    def wordPattern(self, pattern, s):
        d = {}
        hSet = set()
        s = s.split()

        if len(s)<=0 or len(s)!=len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] not in d:
                if s[i] not in hSet:
                    d[pattern[i]] = s[i]
                else:
                    return False
                hSet.add(s[i])            
            else:
                if d[pattern[i]]!=s[i]:
                    return False
        return True 
                
        