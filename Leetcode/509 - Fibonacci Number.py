# https://leetcode.com/problems/fibonacci-number/
# Tags - Array

class Solution:
    def fib(self, N: int) -> int:
        mapme = dict()
        
        def inner(n):
            if n in mapme:
                return mapme[n]
            elif n==1:
                return 1
            elif n==0:
                return 0
            # Set the values in dictionary
            mapme[n] = inner(n-1)+inner(n-2)
            # Return a value
            return mapme[n]
            
        return inner(N)