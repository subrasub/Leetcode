class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return
        
        elif len(nums)==1:
            return nums[0]
        
        elif max(nums)<0:
            return max(nums)
        
        s=0;
        l_max = 0;
        
        for i in range(len(nums)):
            if s+nums[i]>0:
                s+=nums[i] 
                l_max = max(s, l_max)
            else:
                s = 0
        return l_max