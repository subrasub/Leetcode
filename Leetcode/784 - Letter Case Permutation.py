# https://leetcode.com/problems/letter-case-permutation/
# Tags - String

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = ['']
        
        for i in S: 
            if i.isalpha():
                res = [k+i.lower() for k in res] + [k+i.upper() for k in res]
            else:
                res = [k+i for k in res]
        
        return res