class Solution:
    def rob(self, nums: List[int]) -> int:
        def robFrom(i, nums):
            if i>=len(nums):
                return 0

            if i in self.table:
                return self.table[i]

            self.table[i] = max(robFrom(i+1, nums), robFrom(i+2, nums) + nums[i])

            return self.table[i]

        self.table = {}
        return robFrom(0, nums)