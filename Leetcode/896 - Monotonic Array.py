# https://leetcode.com/problems/monotonic-array

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        def cmp(a, b):
            return int(a>b)-int(a<b)
        
        val = 0
        for i in range(len(A)-1):
            temp = cmp(A[i], A[i+1])
            
            if temp:
                if temp != val != 0:
                    return False
                val = temp
        
        return True