class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        while left<right:
            mid = right + (left-right)//2
            if sum((num - 1) // mid + 1 for num in nums) <= threshold:
                right = mid
            else:
                left = mid + 1

        return left