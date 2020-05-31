# https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxCurrent = maxGlobal = nums[0]
        
        for i in range(1, len(nums)):
            maxCurrent = max(nums[i], maxCurrent+nums[i])
            if maxCurrent > maxGlobal:
                maxGlobal = maxCurrent
        
        return maxGlobal
