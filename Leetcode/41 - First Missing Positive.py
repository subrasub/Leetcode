class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 1

        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i]>len(nums):
                nums[i] = 1

        for i in range(len(nums)):
            val = abs(nums[i])

            if val == len(nums):
                nums[0] = -abs(nums[0])
            else:
                nums[val] = -abs(nums[val])

        for i in range(1, len(nums)):
            if nums[i]>0:
                return i

        if nums[0]>0:
            return len(nums)

        return len(nums)+1