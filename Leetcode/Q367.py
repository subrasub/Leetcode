# https://leetcode.com/problems/valid-perfect-square/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=1
        while((i*i)<=num):
            if (num/i == i) and (num % i ==0):
                return True
            i = i+1
        return False
