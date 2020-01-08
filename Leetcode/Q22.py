class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        # use backtracking to add parantheses 
        def compute(paran, left, right):
            if len(paran) == n*2:
                res.append(paran)
                return
            
            if left < n:
                compute(paran+'(', left+1, right)
                
            if right < left:
                compute(paran+')', left, right+1)
        
        compute('', 0, 0)
        return res
        
            
                
            
