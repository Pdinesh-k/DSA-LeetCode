class Solution(object):
    def reverseWords(self, s):
        st = ""
        string = s.split()
        length = len(string)
        i = length-1
        while(i>=0):
            st+=string[i]+" "
            i-=1
        return st.strip()

        