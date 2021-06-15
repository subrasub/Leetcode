# https://leetcode.com/problems/3sum/
# Tags - Array, Two Pointers

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums, val, left, right):
            while left < right:
                threeSum = nums[left]+nums[right] + val

                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([val, nums[left], nums[right]])
                    left += 1

                    while left<right and nums[left] == nums[left-1]:
                        left += 1
        if not nums:
            return []

        res = []
        nums.sort()

        for index, val in enumerate(nums):
            if index>0 and val == nums[index-1]:
                continue

            left, right = index+1, len(nums)-1
            twoSum(nums, val, left, right)

        return res
