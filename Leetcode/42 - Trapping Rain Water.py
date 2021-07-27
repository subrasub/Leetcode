class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        res = 0
        leftMax = [0]*len(height)
        rightMax = [0]*len(height)
        maxL = maxR = 0

        for i in range(len(height)):
            maxL = max(maxL, height[i])
            leftMax[i] = maxL

        for i in range(len(height)-1, -1, -1):
            maxR = max(maxR, height[i])
            rightMax[i] = maxR

        for index in range(len(height)):
            res += min(leftMax[index], rightMax[index]) - height[index]

        return res

