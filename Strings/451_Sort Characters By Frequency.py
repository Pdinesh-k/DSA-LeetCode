class Solution(object):
    def romanToInt(self, s):
        dictionary = {"I" : 1 , "V" : 5 , "X" : 10,"L" : 50 , "C" : 100 , "D" : 500 , "M" : 1000}
        sum = 0
        length = len(s)
        i = 0
        while i<length:
            if(i+1<length and dictionary[s[i]] < dictionary[s[i+1]]):
                sum+=dictionary[s[i+1]]-dictionary[s[i]]
                i+=2
            else:
                sum+=dictionary[s[i]]
                i+=1
        return sum



        