class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        count = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            elif s[i] == ')':
                if count == 0:
                    s[i] = ""
                else:
                    count -= 1
        
        i = len(s) - 1
        
        while i>=0 and count>0:
            if s[i] == '(':
                s[i] = ""
                count -= 1
            i -= 1
        
        return ''.join(s)

