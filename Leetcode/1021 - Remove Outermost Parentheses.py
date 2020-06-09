# https://leetcode.com/problems/remove-outermost-parentheses/
# Tags - Stack

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        item = []
        para = 0
        
        for i in S:
            if i == '(':
                para += 1
                if para > 1:
                    item.append('(')
            elif i== ')':
                para -= 1
                if para != 0:
                    item.append(')')
            
        return ("".join(item))