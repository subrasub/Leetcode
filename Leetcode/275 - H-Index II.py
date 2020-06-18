# https://leetcode.com/problems/h-index-ii/
# Tags - Binary Search

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def binSearch(nums, l, r):
            while l<=r:
                mid = l + (r-l) // 2
                if nums[mid] < (len(nums) - mid):
                    l = mid+1
                else:
                    r = mid-1
            return len(nums)-l
                    
        return binSearch(citations, 0, len(citations)-1)
