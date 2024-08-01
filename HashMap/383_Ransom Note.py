class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count = Counter(magazine)

        for i in ransomNote:
            if i not in magazine or count[i] == 0:
                return False
            else:
                count[i]-=1
        return True
            

        