# https://leetcode.com/problems/minimum-time-visiting-all-points/
# Tags - Array, Geometry

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """
        x+1 and y+1
        x+1 and y
        y+1 and x
        """
        
        res = 0
        x1, y1 = points[0]
        
        for i in range(1, len(points)):
            x2, y2 = points[i]
            res += max(abs(y2-y1), abs(x2-x1))
            x1, y1 = x2, y2
        
        return res
