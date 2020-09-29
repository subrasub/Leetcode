# https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: 
            return 0
        
        maxP = nums[0]
        minP = nums[0]
        res = maxP
        
        for i in range(1, len(nums)):
            temp = max(nums[i], maxP*nums[i], minP*nums[i])
            minP = min(nums[i], maxP*nums[i], minP*nums[i])
            
            maxP = temp
            
            res = max(maxP, res)
        
        return res