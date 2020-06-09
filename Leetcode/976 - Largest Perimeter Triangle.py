# https://leetcode.com/problems/largest-perimeter-triangle/
# Tags - Math, Sort

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        if not A: 
            return 0
        
        A.sort()
        A = A[::-1]
        
        for i in range(2, len(A)):
            if A[i] + A[i-1] > A[i-2]:
                return A[i]+A[i-1]+A[i-2]
        return 0
            
