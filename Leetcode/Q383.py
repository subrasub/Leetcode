# https://leetcode.com/problems/ransom-note/
    
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        table = {}
        
        for i in magazine: 
            if i not in table:
                table[i] = 1
            else:
                table[i] += 1
        
        for i in ransomNote: 
            if i not in table:
                return False
            elif table[i] == 0:
                return False
            else:
                table[i] -= 1
        return True
