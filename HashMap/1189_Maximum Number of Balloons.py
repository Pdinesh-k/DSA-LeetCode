class Solution(object):
    def maxNumberOfBalloons(self, text):
        hash = {"b" : 0,"a":0,"l":0,"o":0,"n":0}
        for i in range(0,len(text)):
            if text[i] in hash:
                hash[text[i]]+=1

        hash['l'] //= 2
        hash['o'] //= 2
        return min(hash.values())
            


        