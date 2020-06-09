# https://leetcode.com/problems/split-a-string-in-balanced-strings/
# Tags - String, Greedy

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        track = 0
        res = 0
        
        for i in s:
            if i == 'R':
                track += 1
            else:
                track -= 1
            
            if track == 0:
                res += 1
                
        return res