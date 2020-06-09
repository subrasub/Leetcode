# https://leetcode.com/problems/3sum/
# Tags - Array, Two Pointers

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []
        ans = []
        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l= i+1
            r = len(nums) - 1
            
            while (l<r):
                res = nums[l] + nums[r] + nums[i]
                
                if res<0:
                    l+=1 
                elif res>0:
                    r -= 1
                else:
                    ans.append((nums[l], nums[r], nums[i]))
                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    while l<r and nums[r-1] == nums[r]:
                        r -= 1
                    l+=1
                    r-=1
        return ans
        