# https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)

        res[0] = 1
        for i in range(1, len(nums)):
            res[i] = res[i-1]*nums[i-1]

        right = 1
        for i in reversed(range(len(nums))):
            res[i] = res[i]*right
            right = right*nums[i]

        return res