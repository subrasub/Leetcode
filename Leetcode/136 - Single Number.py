# https://leetcode.com/problems/single-number/
# Tags - Hash Table, Bit Manipulation

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums: 
            res ^= i
        
        return res
