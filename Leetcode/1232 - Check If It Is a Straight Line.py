# https://leetcode.com/problems/check-if-it-is-a-straight-line/
# Tags - Array, Math, Geometry

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x0, y0) = coordinates[0]
        (x1, y1) = coordinates[1]
        
        for x,y in coordinates: 
            if (y - y1)*(x1 - x0) != (x - x1)*(y1 - y0):
                return False
        return True
