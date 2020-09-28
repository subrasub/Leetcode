# https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [0]*len(nums), [0]*len(nums)
        res = []
            
        left[0] = 1
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1]
        
        right[len(nums)-1] = 1
        for i in reversed(range(len(nums)-1)):
            right[i] = right[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            res.append(left[i]*right[i])
        
        return res