# https://leetcode.com/problems/convert-a-number-to-hexadecimal
# Tags - Bit Manipulation

class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return '0'
        
        table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}     
        res = []
        s = ""
        
        if num<0:
            num += 2**32
            
        while(num != 0):
            r = num % 16
            res.append(r)
            num = num // 16
        
        
        for i in res[::-1]:
            
            if i in table:
                s+=table[i]
        
        return s
