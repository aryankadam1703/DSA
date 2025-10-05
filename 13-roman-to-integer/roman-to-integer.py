class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        l=len(s)
        sum=0
        prev=0
        for i in reversed(s):
            curr=dict[i]
            if curr>=prev:
                sum+=curr
            else:
                sum-=curr
            prev=curr
        return sum