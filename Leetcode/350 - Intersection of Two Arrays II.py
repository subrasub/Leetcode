# https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Tags - Hash Table, Two Pointers, Binary Search, Sort

from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list((Counter(nums1) & Counter(nums2)).elements())
