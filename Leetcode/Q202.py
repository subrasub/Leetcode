# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        table = {}
        
        while(n!=1):
            if n not in table:
                table[n] = 1
                n = sum(int(i)**2 for i in str(n))
            else:
                return False
        return True

