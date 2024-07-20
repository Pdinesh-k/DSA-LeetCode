class Solution(object):
    def isIsomorphic(self, s, t):
        d = {}
        hSet = set()
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]

            if s_char not in d:
                if t_char in hSet:
                    return False
                
                d[s_char] = t_char
                hSet.add(t_char)

            else:
                if t_char != d[s_char]:
                    return False
        return True





        

        