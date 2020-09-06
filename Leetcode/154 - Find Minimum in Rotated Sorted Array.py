# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1
        
        while start<end:
            mid = start + (end-start)//2
            
            if nums[mid] < nums[end]:
                end = mid
            elif nums[mid] > nums[end]:
                start = mid+1
            else: 
                end -= 1
        
        return nums[start]