class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        parenthesis = {'}': '{', ']': '[', ')': '('}
        
        for ch in range(len(s)): 
            
            if s[ch] in parenthesis:  
                if not stack or stack.pop() != parenthesis[s[ch]]:
                    return False
            elif s[ch] in parenthesis.values():
                stack.append(s[ch])
                
        return not stack            
                