# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        if count.most_common()[0][1] > (len(nums))//2:
            return count.most_common()[0][0]
