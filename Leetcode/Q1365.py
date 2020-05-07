# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
    
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        table = {}
        res = []
        
        for index, val in enumerate(sorted(nums)):
            table.setdefault(val, index)
        
        for i in nums:
            res.append(table[i])
        
        return res
                
