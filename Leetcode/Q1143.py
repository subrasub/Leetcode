class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(A, B, i, j, arr):
            if arr[i][j] is not '*':
                return arr[i][j]
            
            if not i or not j:
                res = 0
                
            elif A[i-1] == B[j-1]:
                res = 1 + lcs(A, B, i-1, j-1, arr)
                
            elif A[i-1] != B[j-1]:
                res = max(lcs(A, B, i-1, j, arr), lcs(A, B, i, j-1, arr))
            
            arr[i][j] = res
            return res
        
        res = 0
        
        arr = [['*']*(len(text2)+1)]*(len(text1)+1)
                
        return lcs(list(text1), list(text2), len(text1), len(text2), arr)
        
            
