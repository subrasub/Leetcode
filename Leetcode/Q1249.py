class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = []
        
        for i in range(0,len(s)):
            if s[i] == '(':
                stack.append(i)
                res += s[i]
                
            elif s[i] == ')':
                if not stack:
                    res += '*'
                else:
                    stack.pop()
                    res += s[i]
            else:
                res += s[i]
        
        for i in stack:
            res[i] = '*'
            
        return ''.join(k for k in res if k!='*')
                    
