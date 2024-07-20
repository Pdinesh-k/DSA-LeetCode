class Solution(object):
    def groupAnagrams(self, strs):
        dic = {}
        for i in strs:
            sort = "".join(sorted(i))
            if sort in dic:
                dic[sort].append(i)
            else:
                dic[sort] = [i]
        return dic.values()







        