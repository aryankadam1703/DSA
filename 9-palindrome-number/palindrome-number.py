class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        if x == x[::-1]:
            return True
        return False

        # check = lambda val: False if val < 0 else str(val) == str(val)[::-1]
        # return check(x)