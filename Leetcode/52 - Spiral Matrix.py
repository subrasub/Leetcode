# https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: 
            return
        
        R = len(matrix)
        C = len(matrix[0])
        res = []
        
        seen = [[False]*C for _ in matrix]
        
        row = col = d = 0
        
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        
        for _ in range(R*C):
            res.append(matrix[row][col])
            seen[row][col] = True
            
            cr = row + dr[d]
            cc = col + dc[d]
            
            if (0 <= cr < R) and (0 <= cc < C) and not seen[cr][cc]:
                row, col = cr, cc
            else:
                d = (d+1)%4
                row, col = row + dr[d], col + dc[d]
        
        return res
                