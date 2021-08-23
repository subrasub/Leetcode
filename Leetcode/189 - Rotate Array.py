class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def helper(nums, start, end):
            while start<end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        k = k % len(nums)
        helper(nums, 0, len(nums)-1)
        helper(nums, 0, k-1)
        helper(nums, k, len(nums)-1)