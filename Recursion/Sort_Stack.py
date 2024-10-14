class Solution:   
    def pops(self,s,element):
        if len(s)==0 or s[-1]<=element:
            s.append(element)
        else:
            top = s.pop()
            self.pops(s,element)
            s.append(top)
        
    def Sorted(self, s):
        if len(s)>0:
            top = s.pop()
            self.Sorted(s)
            self.pops(s,top)