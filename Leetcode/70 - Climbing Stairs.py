# https://leetcode.com/problems/climbing-stairs
# Tags - Dynamic Programming

from collections import defaultdict
class Solution:
    def climbStairs(self, n: int) -> int:
        def calc(i, n, table):
            if i>n:
                return 0
            if i == n:
                return 1
            
            if table[i]:
                return table[i]
            
            table[i] = calc(i+1, n, table) + calc(i+2, n, table)
            return table[i]
        
        self.table = defaultdict(list)
        return calc(0, n, self.table)    
