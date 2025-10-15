class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Correct code for limited input
        # if s=="":
        #     return 0
        # return len(max([s[i:j] for i in range(len(s)) for j in range(i+1,len(s)+1) if len(set(s[i:j])) == len(s[i:j])],key=len))

        res=0
        for i in range(len(s)):
            seen=set()
            for j in range(i,len(s)):
                if s[j] in seen:
                    break
                else:
                    seen.add(s[j])
                    res=max(res,j-i+1)
        return res