# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor: 
            return image
        
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        
        def paint(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1:
                    paint(r-1, c)
                if c >= 1: 
                    paint(r, c-1)
                if r+1 < R:
                    paint(r+1, c)
                if c+1 < C:
                    paint(r, c+1)
                
        paint(sr, sc)
        return image
