# https://leetcode.com/problems/counting-bits/
# Tags - Dynamic Programming, Bit Manipulation

class Solution:
    def countBits(self, num: int) -> List[int]:
        res=[0 for i in range(num+1)]        
        
        for i in range(1, num+1):
            n = i
            n = n & 1
            if n==0:
                res[i] = res[i >> 1]
            else:
                res[i] = 1 + res[i-1]
            
        return res