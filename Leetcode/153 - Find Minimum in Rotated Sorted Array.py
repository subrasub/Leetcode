class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        left, right = 0, len(nums)-1

        # no rotation
        if nums[0] < nums[right]:
            return nums[0]

        while (left <= right):
            mid = left + (right-left)//2

            if nums[mid]>nums[mid+1]:
                return nums[mid+1]

            elif nums[mid-1]>nums[mid]:
                return nums[mid]

            elif nums[mid]>nums[0]:
                left = mid + 1
            else:
                right = mid - 1
