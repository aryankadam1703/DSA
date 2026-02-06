class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        output = ''
        min_s = min(strs,key=len)
        for ch in range(len(min_s)):
            count = 0
            for j in strs:
                if min_s[ch] == j[ch]:
                    count+=1
            
            if count == len(strs):
                output += min_s[ch]
            else:
                break
        return output