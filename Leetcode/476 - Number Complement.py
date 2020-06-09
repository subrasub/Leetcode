# https://leetcode.com/problems/number-complement/
# Tags - Bit Manipulation

class Solution:
    def findComplement(self, num: int) -> int:
        i=1
        while i<=num:
            i = i<<1

        return num^(i-1)
