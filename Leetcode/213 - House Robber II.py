class Solution:
    def rob(self, nums: List[int]) -> int:
        def robFrom(nums):
            rob1, rob2 = 0, 0

            for i in nums:
                val = max(i + rob1, rob2)
                rob1 = rob2
                rob2 = val
            return rob2

        return max(nums[0], robFrom(nums[1:]), robFrom(nums[:-1]))