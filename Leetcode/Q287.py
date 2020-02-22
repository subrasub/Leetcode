# https://leetcode.com/problems/find-the-duplicate-number/
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)-len(set(nums))
        return ((sum(nums) - sum(set(nums)))//n) 
        
