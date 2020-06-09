# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Tags - Array, Binary Search

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while(left<right):
            mid = (left+right)//2
            if(nums[mid] > nums[right]):
                left = mid+1
            else: 
                right = mid
        
        
        offset = left
        left = 0
        right = len(nums)-1
        
        while(left <= right):
            mid = (left+right)//2
            originalMid = (mid+offset) % len(nums)
            
            if(nums[originalMid] == target):
                return originalMid
            if(nums[originalMid] > target):
                right = mid-1
            else:
                left = mid+1
                
        return -1