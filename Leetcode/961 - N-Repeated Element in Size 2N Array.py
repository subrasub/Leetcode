# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
# Tags - Hash Map

class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        if A==[]:
            return None
        res=[]
        for x in A:
            if x in res:
                return x
            else:
                res.append(x)