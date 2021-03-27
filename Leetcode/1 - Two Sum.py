class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    arr = {}
    for index, val in enumerate(nums):
      k = target - val
      if k in arr:
        return [arr[k], index]
      else:
        arr[val] = index
    return