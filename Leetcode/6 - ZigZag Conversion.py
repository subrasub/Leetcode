# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows==len(s):
            return s
        
        res = ['']*numRows
        
        index = 0
        move = 1
        
        for letter in s:
            res[index] += letter
            
            if index == 0:
                move = 1
            
            elif index == numRows-1:
                move = -1
            
            index += move
            
                
        return ''.join(res)