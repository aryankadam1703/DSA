class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        c = min(strs, key=len)
        for i in range(len(strs)):
            for j in range(len(c)):
                if c[j] != strs[i][j]:
                    c = c[:j]
                    break
        return c