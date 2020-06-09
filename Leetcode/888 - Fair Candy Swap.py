# https://leetcode.com/problems/fair-candy-swap/submissions/
# Tags - Array

class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        # can come up with a math soln
        S = set(B)
        sum_A = sum(A)
        sum_B = sum(B)
        for i in A:
            if (i+ (sum_B-sum_A)/2) in S:
                return [i, math.floor(i+ (sum_B-sum_A)/2)]