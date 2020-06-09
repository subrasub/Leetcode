# https://leetcode.com/problems/rank-transform-of-an-array/
# Tags - Array

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        table = {}
        res = []
        
        for i in sorted(arr):
            table.setdefault(i, len(table)+1)
        
        for i in arr:
            res.append(table[i])
            
        return res
