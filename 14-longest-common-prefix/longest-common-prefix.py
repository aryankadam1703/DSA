class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output=""
        s=min(strs,key=len)
        for i in range(len(s)):
            count=0
            for j in strs:
                if s[i]==j[i]:
                    count+=1
            if count==len(strs):
                output+=s[i]
            else:
                break
        return output
        