# https://leetcode.com/problems/single-element-in-a-sorted-array/
# Tags - Array

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)