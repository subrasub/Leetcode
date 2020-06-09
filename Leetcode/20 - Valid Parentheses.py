# https://leetcode.com/problems/valid-parentheses/
# Tags - String, Stack

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        
        if len(s)%2 != 0:
            return False
        
        paran = {'(': ')', '[': ']', '{': '}'}
        stack = []
        
        for i in s:
            if i in paran:
                stack.append(paran[i])
                
            else:
                if not stack or stack.pop() != i:
                    return False
            
        return len(stack)==0
