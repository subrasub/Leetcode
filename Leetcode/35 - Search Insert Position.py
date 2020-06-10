# https://leetcode.com/problems/search-insert-position/
# Tags - Array, Binary Search

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        
        for i in range(len(nums)):
            mid = (left+right)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else: 
                left = mid + 1
        return left
