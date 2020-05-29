# https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        table = []
        
        for i in range(len(num)):
            while k>0 and table:
                if num[i] < table[-1]:
                    k -= 1
                    table.pop()
                else:
                    break
            table.append(num[i])
        
        while k != 0:
            k -= 1
            table.pop()
        
        while table:
            if table[0] == '0':
                table = table[1:]
            else:
                break
        
        return ''.join(table) or '0'
