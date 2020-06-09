# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# Tags - Bit Manipulation

class Solution:
    def numberOfSteps (self, num: int) -> int:
        i=0
        while(num):
            if num%2==0:
                num = num//2
            else:
                num -= 1
            
            i+=1
        return i
