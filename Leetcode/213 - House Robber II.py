class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            r1 = 0
            r2 = 0

            for val in nums:
                temp = r1
                r1 = max(val+r2, r1)
                r2 = temp

            return r1

        if not nums:
            return 0

        if len(nums)==1:
            return nums[0]

        return max(helper(nums[:-1]), helper(nums[1:]))