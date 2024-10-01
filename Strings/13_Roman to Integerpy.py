class Solution(object):
    def myAtoi(self, s):

        num = "0123456789"
        string = ""

        for i in s:
            if i == " " and len(string)==0:
                continue
            
            if i!=" " and (i in "+-" or i in num) and len(string)==0:
                string+=i
            elif i in num:
                string+=i
            else:
                break
            
        if string == "" or (len(string)==1 and string in "+-"):
            return 0
        else:
            if int(string)<-(2**31):
                return -(2**31)
            elif int(string)>(2**31-1):
                return (2**31-1)
            else:
                return int(string)





        