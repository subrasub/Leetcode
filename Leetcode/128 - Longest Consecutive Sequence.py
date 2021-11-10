class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        items = set(nums)

        for num in nums:
            if num-1 not in items:
                curr = num
                streak = 1

                while curr+1 in items:
                    curr += 1
                    streak += 1

                res = max(res, streak)

        return res