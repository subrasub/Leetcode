# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height)-1
        maxArea = 0
        
        while start<end:
            lim = min(height[start], height[end])
            area = (end-start) * lim
            
            if area>maxArea: 
                maxArea = area
            
            if height[start]<height[end]:
                start += 1
            else:
                end -= 1
                
        return maxArea