# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# Tags - Stack Greedy

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        if not str:
            return 0
        
        left = 0
        right = 0
        
        for i in S:
            if i == '(':
                left += 1
            else:
                if left > 0:
                    left -= 1
                else:
                    right += 1
                
        return left+right
