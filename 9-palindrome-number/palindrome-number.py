class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        check = lambda val: False if val < 0 else str(val) == str(val)[::-1]
        return check(x)