# https://leetcode.com/problems/intersection-of-two-arrays
# Tags - Hash Table, Two Pointers, Binary Search, Sort

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s = set(nums1)
        t = set(nums2)
        v = list(s.intersection(t))
        return v