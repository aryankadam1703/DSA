class Solution(object):
    def romanToInt(self, s, i=0):
        """
        :type s: str
        :rtype: int
        """
        roman_num = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        t=0
        prev = 0
        for char in reversed(s):
            curr = roman_num[char]
            if curr < prev:
                t-=curr
            else:
                t+=curr
                prev = curr
        return t

        